#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.extract import extract_fns_user_type
from extract_utils.extract_star import extract_star_firmware
from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/motorola',
    'hardware/qcom-caf/wlan',
    'vendor/motorola/sm6225-common',
    'vendor/qcom/opensource/display',
]

lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
}

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/android.hardware.nfc@1.2-service.sec.rc': blob_fixup()
        .regex_replace('sec', 'samsung')
        .regex_replace('class hal', 'override\n    class hal'),
    (
        'vendor/lib64/camera/components/com.qti.node.gpu.so',
        'vendor/lib64/com.qti.feature2.gs.so',
        'vendor/lib64/com.qti.feature2.rt.so',
        'vendor/lib64/hw/camera.qcom.so',
        'vendor/lib64/hw/com.qti.chi.override.so',
    ): blob_fixup()
        .binary_regex_replace(b'camera.mot.is.coming.cts', b'vendor.camera.coming.cts'),
}  # fmt: skip

extract_fns: extract_fns_user_type = {
    r'(bootloader|radio)\.img': extract_star_firmware,
}

module = ExtractUtilsModule(
    'rhode',
    'motorola',
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    extract_fns=extract_fns,
    add_firmware_proprietary_file=True,
    add_generated_carriersettings=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sm6225-common', module.vendor
    )
    utils.run()
