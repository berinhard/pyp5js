#!/usr/bin/env bash

################################################################################
#           Checks if required assets for pyp5js to work are present           #
#                                                                              #
#                                                Created on 31/03/2023         #
################################################################################

script_path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
required_assets=$(cat "$script_path/required_assets.txt")
semver_regex='([0-9]+)\.([0-9]+)\.([0-9]+)(-([0-9A-Za-z-]+(\.[0-9A-Za-z-]+)*))?(\+[0-9A-Za-z-]+)?'

for asset in $required_assets; do
    sanitized_asset=$(echo "$asset" | sed -r "s/$semver_regex/*/g")
    if ! compgen -G "$sanitized_asset" > /dev/null; then
        echo "ERROR: Required $sanitized_asset is missing in the build"
        exit 1
    fi
done
