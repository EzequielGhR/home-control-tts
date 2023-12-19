#!/bin/bash
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")" ; pwd -P )
cd "$parent_path"

ENV_PATH = ".hcenv/bin/activate"

function hc-lights() {
    all=false
    while [ "${1:-}" != "" ]; do
        case $1 in
            -s| --status)
                shift
                status=$1
                ;;
            -i| --identifier)
                shift
                identifier=$1
                ;;
            -a| --all)
                all=true
                ;;
        esac
        shift
    done;
    source $ENV_PATH
    if [ $all == true ]; then
        echo "all lights $status"
        python -m tts_script --all True --status $status --identifier ""
    else
        echo "only $identifier $status"
        python -m tts_script --all False --status $status --identifier $identifier
    fi
    deactivate
}

function hc-lights-intensity() {
    all=false
    color="white"
    value=100
    while [ "${1:-}" != "" ]; do
        case $1 in
            -v| --value)
                shift
                value=$1
                ;;
            -i| --identifier)
                shift
                identifier=$1
                ;;
            -a| --all)
                all=true
                ;;
            -c| --color)
                shift
                color=$1
                ;;
        esac
        shift
    done;
    source $ENV_PATH
    if [ $all == true ]; then
        echo "all lights $color at $value %"
        python -m tts_script --all True --color $color --value $value --identifier ""
    else
        echo "only $identifier $color at $value %"
        python -m tts_script --all False --color $color --value $value --identifier $identifier
    fi
    deactivate
}

function hc-music() {
    band=""
    song=""
    language=""
    while [ "${1:-}" != "" ]; do
        case $1 in
            -s| --song)
                shift
                song=$1
                ;;
            -b| --band)
                shift
                band=$1
                ;;
            -l| --language)
                shift
                language=$1
                ;;
        esac
        shift
    done;
    source $ENV_PATH
    python -m tts_script --song "${song}" --band "${band}" --language "${language}"
    deactivate
}