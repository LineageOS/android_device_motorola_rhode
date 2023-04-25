#
# Copyright (C) 2022-2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from sm6225-common
include device/motorola/sm6225-common/BoardConfigCommon.mk

DEVICE_PATH := device/motorola/rhode

# Bootloader
TARGET_BOOTLOADER_BOARD_NAME := rhode

# Display
TARGET_SCREEN_DENSITY := 400

# HIDL
ODM_MANIFEST_SKUS += b
ODM_MANIFEST_B_FILES := $(DEVICE_PATH)/sku/manifest_b.xml

# Kernel
TARGET_KERNEL_CONFIG += vendor/ext_config/rhode-default.config

# Kernel Modules - Vendor Boot
BOARD_VENDOR_RAMDISK_KERNEL_MODULES_LOAD := $(strip $(shell cat $(DEVICE_PATH)/vendor_boot.modules.load))
BOOT_KERNEL_MODULES := $(BOARD_VENDOR_RAMDISK_KERNEL_MODULES_LOAD)

# Recovery
TARGET_RECOVERY_UI_MARGIN_HEIGHT := 100

# Security patch level
VENDOR_SECURITY_PATCH := 2023-03-01

# Inherit from the proprietary version
include vendor/motorola/rhode/BoardConfigVendor.mk
