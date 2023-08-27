#!/usr/bin/env bash
### every exit != 0 fails the script
set -e

echo "Install some common tools for further installation"
apt-get update
apt-get install -y vim wget net-tools locales bzip2 procps apt-utils \
    python3-numpy #used for websockify/novnc

echo "Install tools for OpenGL development with c++"
apt-get install -y clang libglfw3-dev libglm-dev libglew-dev \
    git valgrind cmake gdb

apt-get clean -y

echo "generate locales für en_US.UTF-8"
echo "en_US.UTF-8 UTF-8" > /etc/locale.gen
locale-gen
