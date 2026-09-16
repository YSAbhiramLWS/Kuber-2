**Task 1.2 — Multi-Cluster Client–Server Communication Using Kubernetes and Docker**
1. Objective

Establish communication between two independent client Pods and one server Pod, where:

Both clients run inside one Kubernetes cluster.

The server runs inside a separate Kubernetes cluster.

Both clusters are created using **kind** (Kubernetes in Docker).

Docker provides the underlying container environment.

Kubernetes manages the Pods, Deployment, and Service.

The clients communicate with the server using HTTP.

The server exposes its application through a **NodePort** Service.

Commands used:-
1) & "$env:USERPROFILE\bin\kind.exe" version (Checks the installed version of KIND)

2) & "$env:USERPROFILE\bin\kind.exe" create cluster --name client-cluster (Creates a client cluster)

3) kubectl config get-contexts (Verify clusters)

4) kubectl config use-context kind-client-cluster (Switch to client cluster)

5) kubectl get nodes (Verify nodes)

6) & "$env:USERPROFILE\bin\kind.exe" create cluster --name server-cluster --config .\server-cluster-config.yaml (create a server cluster)

7) kubectl config use-context kind-server-cluster (Switch to server cluster)

8) docker build -t smo-task12-server:latest .\kuber-2\server (Build server docker image)

9) & "$env:USERPROFILE\bin\kind.exe" load docker-image smo-task12-server:latest --name server-cluster (Copies locally built image into the nodes of server cluster)

10) kubectl apply -f .\server\server-deployment.yaml (deploy server)

11) kubectl apply -f .\server\server-service.yaml (create service)

12) kubectl get service (verify service)

13) kubectl get endpoints smo-task12-service (verify service endpoints)

14) curl.exe http://localhost:30080/ (test the server)

15) docker build -t smo-task12-client:latest .\kuber-2\client (build client image)

16) & "$env:USERPROFILE\bin\kind.exe" load docker-image smo-task12-client:latest --name client-cluster (load image into client cluster)

17) kubectl apply -f .\client\client-pods.yaml (deploy both clients)

18) kubectl exec -it smo-task12-client-1/client-2 -- python client.py (start client-1/2)

19) kubectl exec smo-task12-client-1 -- curl -v http://172.18.0.6:30080/ (verify communication from client side)

20) docker inspect client-cluster-control-plane --format "{{json .NetworkSettings.Networks}}" (docker inspect client-cluster-control-plane --format "{{json .NetworkSettings.Networks}}")

<img width="220" height="599" alt="image" src="https://github.com/user-attachments/assets/c800e715-3442-4152-a497-cbd795dd2878" />
