
REMOTE_BUCKET = "http://localhost:9000/minio/my-dataset-s3-bucket"
PATH_FORMAT = "{remote_bucket}/InCabin-demo/videos/{stream_name}"

video_streams = [
    "1538523280_cam-rgb-1.avi",
    "1537396942_cam-rgb-2.avi",
]

video_full_paths = []

for stream in video_streams:
    fullpath = PATH_FORMAT.format(remote_bucket=REMOTE_BUCKET, stream_name=stream)
    video_full_paths.append(fullpath)

video_full_paths_option_str = ",".join(['"{p}"'.format(p=p) for p in video_full_paths])

cmd = ('flyte-cli -p flytekubecondemo2019 -d development -h localhost:30081 --insecure execute-launch-plan '
       '--urn lp:flytekubecondemo2019:development:workflows.data_preparation_workflow.DataPreparationWorkflow:8cf2d43e1b68aa9ae324dc2e86dbf8852646f865 '
       '-r changhonghsu')

cmd += ' -- video_external_paths=\'[{full_paths}]\''.format(full_paths=video_full_paths_option_str)

print(cmd)
