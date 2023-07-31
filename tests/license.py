from googleapiclient import discovery
import sys

compute_service = discovery.build('compute', 'v1', cache_discovery=False, credentials=None)

IMAGE_NAME = sys.argv[1]
#c0-deeplearning-common-cpu-v20230615-debian-10
IMAGE_PROJECT = sys.argv[2]
#composer-vpc-host-362519


def get_license_codes_from_image():
    request = compute_service.images().get(project=IMAGE_PROJECT, image=IMAGE_NAME).execute()
    return request['licenseCodes']


def query_license_code(license_code):
    request = compute_service.licenseCodes().get(project=IMAGE_PROJECT, licenseCode=license_code).execute()
    licenses = []
    for alias in request["licenseAlias"]:
        license_name = alias["selfLink"].split('/')[-1]
        license_project = alias["selfLink"].split('/')[-4]
        licenses.append(compute_service.licenses().get(project=license_project, license=license_name).execute())
    return licenses


def main():
    if IMAGE_NAME == '':
        print("No Image name provided...")
    else:
        license_codes = get_license_codes_from_image()
        for license_code in license_codes:
            license_code_body = query_license_code(license_code)
            print("License Code: {}\nLicense Body: {}\n\n".format(license_code, license_code_body))


if __name__ == '__main__':
    main()