import pulumi
from pulumi_azure_native import storage

import pulumi_azure as azure

account = storage.StorageAccount("yasharstorage634",
resource_group_name="rg-interview",
sku=storage.SkuArgs(name=storage.SkuName.STANDARD_LRS,),
kind=storage.Kind.STORAGE_V2)