Steps to be followed

Trying java auto-instrumention with otel-collector on k8s set-up

![Trace](./Trace.png)
https://opentelemetry.io/docs/instrumentation/java/automatic/

- cd agent
- docker build -t agent-container:0.1.0 .
- cd sample-app
- docker build -t sample-java-app:0.1.0 .

- kind k8s cluster - https://kind.sigs.k8s.io/docs/user/quick-start/

 - ./kind create cluster --config=kind-cluster.yaml
 - kubectl cluster-info --context kind-kind
 - ./kind load docker-image agent-container:0.1.0
 - ./kind load docker-image sample-java-app:0.1.0
- ./kind load docker-image otel/opentelemetry-collector:0.68.0
- ./kind load docker-image jaegertracing/all-in-one:1.41.0

- docker exec -it $(./kind get clusters | head -1)-control-plane crictl images
- kubectl apply -f objects/jaeger.yml
- kubectl apply -f objects/otel-collector.yml
- kubectl apply -f objects/app-agent.yml
- kubectl get pods
- Sample java app - localhost:4567
- Traces - localhost:16686
- To delete the cluster use (/kind delete cluster)