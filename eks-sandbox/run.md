# test things locally
```bash
python3 -m virtualenv venv
source venv/bin/activate
pip install flask
python3 app.py
pip freeze > requirements.txt
docker build -t http .
docker tag http louiskimlevu/http 
docker push louiskimlevu/http
```

# deploy eks
```bash
export cluster=eksdemo
export region=us-east-1
export account_id=$(aws sts get-caller-identity | jq -r .Account)

eksctl create cluster 
--name $cluster \
--region $region \
--with-oidc \
--version 1.27
--fargate \
--vpc-cidr 10.0.0.0/16 \
--vpc-nat-mode Single
--auto-kubeconfig \
--write-kubeconfig \

vpc_id=$(eksctl get  cluster --region $region $cluster | awk '{print $5}' | grep vpc-)
```
# deploy aws-lb-bcontroller

```bash
eksctl create iamserviceaccount \
  --cluster=$cluster \
  --region $region \
  --namespace=kube-system \
  --name=aws-load-balancer-controller \
  --role-name AmazonEKSLoadBalancerControllerRole_$cluster \
  --attach-policy-arn=arn:aws:iam::$account_id:policy/AWSLoadBalancerControllerIAMPolicy \
  --approve \

helm install aws-load-balancer-controller eks/aws-load-balancer-controller \
  -n kube-system \
  --set clusterName=$cluster \
  --set region=$region \
  --set serviceAccount.create=false \
  --set serviceAccount.name=aws-load-balancer-controller \
  --set vpcId=$vpc_id

kaf k8s_http.yaml
http_service_dns=$(kgs | grep http | awk '{print $4}')
curl $http_service_dns
```

# deploy istio
```bash
eksctl create fargateprofile --namespace istio-system --cluster $cluster --region $region
istioctl install

kubectl annotate service istio-ingressgateway -n istio-system \
  service.beta.kubernetes.io/aws-load-balancer-type=external \
  service.beta.kubernetes.io/aws-load-balancer-nlb-target-type=ip \
  service.beta.kubernetes.io/aws-load-balancer-scheme=internet-facing

kaf k8s_http_istio.yaml
isitio_ingress_dns=$(kgs -n istio-system | grep ingress | awk '{print $4}')
curl -H "Host: test.com" k8s-istiosys-istioing-66a0f46290-e650b8ad96bfe006.elb.us-east-1.amazonaws.com
```

# cleanup
```bash
k delete -f k8s_http_istio.yaml
istioctl uninstall --purge
istio_fp_id=$(eksctl get fargateprofile --cluster $cluster --region us-east-1 | grep istio | awk '{print $1}')
eksctl delete fargateprofile --cluster $cluster --region $region $istio_fp_id
k delete -f k8s_http.yaml
helm uninstall -n kube-system aws-load-balancer-controller
eksctl delete iamserviceaccount --cluster=$cluster --region=$region --name aws-load-balancer-controller
eksctl delete cluster --region=$region $cluster
```
