mkdir -p "$(dirname "$0")/../build"
python "$(dirname "$0")/../build.py" --build true
aws s3 sync ./build s3://$S3_BUCKET --delete --acl public-read
