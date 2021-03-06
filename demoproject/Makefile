export IMAGE_NAME=flytekubecondemo2019
PROJECT=flytekubecondemo2019
DOMAIN=development
VERSION=$(shell ./version.sh)

.PHONY: serialize
serialize:
	FLYTE_PLATFORM_URL=flyte-staging.lyft.net FLYTE_INTERNAL_IMAGE=abc:133 pyflyte -p ${PROJECT} -d ${DOMAIN} --config /app/sandbox.config serialize workflows

.PHONY: register_sandbox_in_container
register_sandbox_in_container:
	env
	pyflyte -p ${PROJECT} -d ${DOMAIN} --config /app/sandbox.config register workflows

.PHONY: register_sandbox
register_sandbox: docker_push
	kubectl delete job register || true
	kubectl create job register --image=docker.io/lyft/${IMAGE_NAME}:${VERSION} -- /opt/flytekit_venv make register_sandbox_in_container

.PHONY: execute_sandbox
execute_sandbox:
	flyte-cli -h localhost:30081 -p flytekubecondemo2019 -d development --insecure execute-launch-plan --urn lp:flytekubecondemo2019:development:workflows.data_preparation_workflow.DataPreparationWorkflow:${VERSION} -r demo -- video_external_paths='["s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/1537396662_cam-rgb-1.avi","s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/1538521877_cam-rgb-1.avi","s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/1538523916_cam-rgb-2.avi"]'

.PHONY: register_staging_in_container
register_staging_in_container:
	pyflyte -p ${PROJECT} -d ${DOMAIN} --config /app/staging.config register workflows


.PHONY: register_staging
register_staging: docker_push
	docker run docker.io/lyft/${IMAGE_NAME}:${VERSION} /opt/flytekit_venv make register_staging_in_container


.PHONY: register_production_in_container
register_production_in_container:
	pyflyte -p ${PROJECT} -d ${DOMAIN} --config /app/production.config register workflows


.PHONY: register_production
register_production: docker_push
	docker run docker.io/lyft/${IMAGE_NAME}:${VERSION} /opt/flytekit_venv make register_production_in_container


.PHONY: execute_staging
execute_staging:
	flyte-cli -h flyte-staging.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.data_preparation_workflow.DataPreparationWorkflow:${VERSION} \
		-r demo -- streams_external_storage_prefix='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/streams' \
		streams_names='["1539471715_cam-rgb-2","1539471904_cam-rgb-1","1539471904_cam-rgb-2","1539475636_cam-rgb-1","1539475636_cam-rgb-2"]'


.PHONY: execute_full_staging
execute_full_staging:
	flyte-cli -h flyte-staging.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.data_preparation_workflow.DataPreparationWorkflow:${VERSION} \
		-r demo -- streams_external_storage_prefix='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/streams' \
		streams_names='["1537396038_cam-rgb-1","1537396038_cam-rgb-2","1537396662_cam-rgb-1","1537396662_cam-rgb-2","1537396790_cam-rgb-1","1537396790_cam-rgb-2","1537396942_cam-rgb-1","1537396942_cam-rgb-2","1538521877_cam-rgb-1","1538521877_cam-rgb-2","1538521964_cam-rgb-1","1538521964_cam-rgb-2","1538522195_cam-rgb-1","1538522195_cam-rgb-2","1538522386_cam-rgb-1","1538522386_cam-rgb-2","1538522615_cam-rgb-1","1538522615_cam-rgb-2","1538522881_cam-rgb-1","1538522881_cam-rgb-2","1538523052_cam-rgb-1","1538523052_cam-rgb-2","1538523280_cam-rgb-1","1538523280_cam-rgb-2","1538523741_cam-rgb-1","1538523741_cam-rgb-2","1538523916_cam-rgb-1","1538523916_cam-rgb-2","1538524089_cam-rgb-1","1538524089_cam-rgb-2","1539390982_cam-rgb-1","1539390982_cam-rgb-2","1539391169_cam-rgb-1","1539391169_cam-rgb-2","1539391321_cam-rgb-1","1539391321_cam-rgb-2","1539391462_cam-rgb-1","1539391462_cam-rgb-2","1539391643_cam-rgb-1","1539391643_cam-rgb-2","1539391807_cam-rgb-1","1539391807_cam-rgb-2","1539391941_cam-rgb-1","1539391941_cam-rgb-2","1539471715_cam-rgb-1","1539471715_cam-rgb-2","1539471904_cam-rgb-1","1539471904_cam-rgb-2","1539475636_cam-rgb-1","1539475636_cam-rgb-2"]'

.PHONY: execute_full_production
execute_full_production:
	flyte-cli -h flyte.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.data_preparation_workflow.DataPreparationWorkflow:${VERSION} \
		-r demo -- streams_external_storage_prefix='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/streams' \
		streams_names='["1537396038_cam-rgb-1","1537396038_cam-rgb-2","1537396662_cam-rgb-1","1537396662_cam-rgb-2","1537396790_cam-rgb-1","1537396790_cam-rgb-2","1537396942_cam-rgb-1","1537396942_cam-rgb-2","1538521877_cam-rgb-1","1538521877_cam-rgb-2","1538521964_cam-rgb-1","1538521964_cam-rgb-2","1538522195_cam-rgb-1","1538522195_cam-rgb-2","1538522386_cam-rgb-1","1538522386_cam-rgb-2","1538522615_cam-rgb-1","1538522615_cam-rgb-2","1538522881_cam-rgb-1","1538522881_cam-rgb-2","1538523052_cam-rgb-1","1538523052_cam-rgb-2","1538523280_cam-rgb-1","1538523280_cam-rgb-2","1538523741_cam-rgb-1","1538523741_cam-rgb-2","1538523916_cam-rgb-1","1538523916_cam-rgb-2","1538524089_cam-rgb-1","1538524089_cam-rgb-2","1539390982_cam-rgb-1","1539390982_cam-rgb-2","1539391169_cam-rgb-1","1539391169_cam-rgb-2","1539391321_cam-rgb-1","1539391321_cam-rgb-2","1539391462_cam-rgb-1","1539391462_cam-rgb-2","1539391643_cam-rgb-1","1539391643_cam-rgb-2","1539391807_cam-rgb-1","1539391807_cam-rgb-2","1539391941_cam-rgb-1","1539391941_cam-rgb-2","1539471715_cam-rgb-1","1539471715_cam-rgb-2","1539471904_cam-rgb-1","1539471904_cam-rgb-2","1539475636_cam-rgb-1","1539475636_cam-rgb-2"]'

.PHONY: train_staging
train_staging:
	flyte-cli -h flyte-staging.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.classifier_train_workflow.ClassifierTrainWorkflow:${VERSION} \
		-r demo -- streams_metadata_path='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/metadata/streams_metadata.json'


.PHONY: evaluate_staging
evaluate_staging:
	flyte-cli -h flyte-staging.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.classifier_evaluate_workflow.ClassifierEvaluateWorkflow:${VERSION} \
		-r demo -- streams_metadata_path='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/metadata/streams_metadata.json'


.PHONY: train_production
train_prodution:
	flyte-cli -h flyte.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.classifier_train_workflow.ClassifierTrainWorkflow:${VERSION} \
		-r demo -- streams_metadata_path='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/metadata/streams_metadata.json'

.PHONY: driver_staging
driver_staging:
	flyte-cli -h flyte-staging.lyft.net -p flytekubecondemo2019 -d development execute-launch-plan \
		--urn lp:flytekubecondemo2019:development:workflows.driver_workflow.DriverWorkflow:${VERSION} \
		-r demo -- streams_external_storage_prefix='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/streams' \
		streams_names='["1537396038_cam-rgb-1","1537396038_cam-rgb-2","1537396662_cam-rgb-1","1537396662_cam-rgb-2","1537396790_cam-rgb-1","1537396790_cam-rgb-2","1537396942_cam-rgb-1","1537396942_cam-rgb-2","1538521877_cam-rgb-1","1538521877_cam-rgb-2","1538521964_cam-rgb-1","1538521964_cam-rgb-2","1538522195_cam-rgb-1","1538522195_cam-rgb-2","1538522386_cam-rgb-1","1538522386_cam-rgb-2","1538522615_cam-rgb-1","1538522615_cam-rgb-2","1538522881_cam-rgb-1","1538522881_cam-rgb-2","1538523052_cam-rgb-1","1538523052_cam-rgb-2","1538523280_cam-rgb-1","1538523280_cam-rgb-2","1538523741_cam-rgb-1","1538523741_cam-rgb-2","1538523916_cam-rgb-1","1538523916_cam-rgb-2","1538524089_cam-rgb-1","1538524089_cam-rgb-2","1539390982_cam-rgb-1","1539390982_cam-rgb-2","1539391169_cam-rgb-1","1539391169_cam-rgb-2","1539391321_cam-rgb-1","1539391321_cam-rgb-2","1539391462_cam-rgb-1","1539391462_cam-rgb-2","1539391643_cam-rgb-1","1539391643_cam-rgb-2","1539391807_cam-rgb-1","1539391807_cam-rgb-2","1539391941_cam-rgb-1","1539391941_cam-rgb-2","1539471715_cam-rgb-1","1539471715_cam-rgb-2","1539471904_cam-rgb-1","1539471904_cam-rgb-2","1539475636_cam-rgb-1","1539475636_cam-rgb-2"]' \
		streams_metadata_path='s3://lyft-modelbuilder/metadata/_FlyteKubeconDemo2019Dataset/metadata/streams_metadata.json'

.PHONY: docker_build
docker_build:
	scripts/docker_build.sh

.PHONY: docker_push
docker_push:
	REGISTRY=docker.io/lyft scripts/docker_build.sh
