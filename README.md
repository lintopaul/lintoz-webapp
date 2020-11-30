This app can read and update user quota comprising of cpu, memory and disk

### Technologies used
* Python 3.8
* Flask 

### Sample Deployment

![GET request](docs/mywebapp-get.png)

![POST request](docs/mywebapp-post.png) 

The deployment above has been done on GKE cluster created out of [terraform module for GKE](https://github.com/terraform-google-modules/terraform-google-kubernetes-engine)
 
 ### Sample deployment
 
```
[lpaul@lions-den webapp]$ gcloud config set project coral-sanctuary-267609
Updated property [core/project].
[lpaul@lions-den webapp]$ gcloud config set compute/zone us-central1
Updated property [compute/zone].
[lpaul@lions-den webapp]$ gcloud container clusters get-credentials lintoz
Fetching cluster endpoint and auth data.
kubeconfig entry generated for lintoz.
[lpaul@lions-den webapp]$ gcloud container images list
NAME
gcr.io/coral-sanctuary-267609/lintoz-webapp
[lpaul@lions-den webapp]$ kubectl create -f ~/1kubernetes/manifests/my-webapp.yaml
deployment.apps/lintoz-webapp created
[lpaul@lions-den webapp]$ kubectl get deployments
NAME            READY   UP-TO-DATE   AVAILABLE   AGE
lintoz-webapp   0/1     1            0           7s
[lpaul@lions-den webapp]$ kubectl get pods
NAME                             READY   STATUS              RESTARTS   AGE
lintoz-webapp-548bcbd459-d7ffd   0/1     ContainerCreating   0          13s
[lpaul@lions-den webapp]$ kubectl describe pod lintoz-webapp-548bcbd459-d7ffd 
Name:         lintoz-webapp-548bcbd459-d7ffd
Namespace:    default
Priority:     0
Node:         gke-lintoz-default-node-pool-c7e6ded5-2bw4/10.128.0.12
Start Time:   Mon, 30 Nov 2020 14:38:49 +0530
Labels:       app=lintoz-webapp
              pod-template-hash=548bcbd459
Annotations:  cni.projectcalico.org/podIP: 10.64.1.12/32
              cni.projectcalico.org/podIPs: 10.64.1.12/32
Status:       Running
IP:           10.64.1.12
IPs:
  IP:           10.64.1.12
Controlled By:  ReplicaSet/lintoz-webapp-548bcbd459
Containers:
  lintoz-webapp-container:
    Container ID:   docker://dbf630ca537dbba3085df1b177214fffafc7d95fd4c5e2edbd4159923f14b37e
    Image:          gcr.io/coral-sanctuary-267609/lintoz-webapp:v1
    Image ID:       docker-pullable://gcr.io/coral-sanctuary-267609/lintoz-webapp@sha256:f570eea25d2774091309e013249bc5ac6bed3c155a2c842f9c30a2bf39aa089a
    Port:           <none>
    Host Port:      <none>
    State:          Running
      Started:      Mon, 30 Nov 2020 14:39:13 +0530
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-w79jg (ro)
Conditions:
  Type              Status
  Initialized       True 
  Ready             True 
  ContainersReady   True 
  PodScheduled      True 
Volumes:
  default-token-w79jg:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-w79jg
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute for 300s
                 node.kubernetes.io/unreachable:NoExecute for 300s
Events:
  Type    Reason     Age        From                                                 Message
  ----    ------     ----       ----                                                 -------
  Normal  Scheduled  <invalid>  default-scheduler                                    Successfully assigned default/lintoz-webapp-548bcbd459-d7ffd to gke-lintoz-default-node-pool-c7e6ded5-2bw4
  Normal  Pulling    <invalid>  kubelet, gke-lintoz-default-node-pool-c7e6ded5-2bw4  Pulling image "gcr.io/coral-sanctuary-267609/lintoz-webapp:v1"
  Normal  Pulled     <invalid>  kubelet, gke-lintoz-default-node-pool-c7e6ded5-2bw4  Successfully pulled image "gcr.io/coral-sanctuary-267609/lintoz-webapp:v1"
  Normal  Created    <invalid>  kubelet, gke-lintoz-default-node-pool-c7e6ded5-2bw4  Created container lintoz-webapp-container
  Normal  Started    <invalid>  kubelet, gke-lintoz-default-node-pool-c7e6ded5-2bw4  Started container lintoz-webapp-container
[lpaul@lions-den webapp]$ kubectl get pods
NAME                             READY   STATUS    RESTARTS   AGE
lintoz-webapp-548bcbd459-d7ffd   1/1     Running   0          35s
[lpaul@lions-den webapp]$ kubectl create -f ~/1kubernetes/manifests/my-webapp-service.yaml 
service/lintoz-webapp-service created
[lpaul@lions-den webapp]$ kubectl get svc
NAME                    TYPE           CLUSTER-IP     EXTERNAL-IP   PORT(S)        AGE
kubernetes              ClusterIP      10.68.0.1      <none>        443/TCP        143m
lintoz-webapp-service   LoadBalancer   10.68.13.146   34.70.237.7   80:32741/TCP   48s
```