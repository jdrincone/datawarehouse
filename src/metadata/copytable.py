import yaml

from src.metadata.paths import Paths

with open(Paths.cred) as file:
    cred = yaml.full_load(file)
cred_aws = cred['aws']


class CopyTable:
    """ Copia de datos desde el bucket del S3 a tabla en Redshift."""

    dataset = (""" copy dataset from
                 's3://jdredshift/r5/dataset.csv' 
                iam_role 'arn:aws:iam::104766822410:role/MiRoleRedshift' 
                delimiter ',' region 'us-east-2' ignoreheader 1;""")
