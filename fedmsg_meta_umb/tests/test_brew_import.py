# Copyright (C) 2017 Red Hat, Inc.
#
# fedmsg_meta_umb is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# fedmsg_meta_umb is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with fedmsg; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
#
# Authors:  Mike Bonnet <mikeb@redhat.com>

import test_brew

class TestBrewImportBuild(test_brew.BrewBase):
    expected_title = 'brew.import.build'
    expected_subti = 'ghostscript-9.07-26.el7 has been imported'
    expected_packages = set(['ghostscript'])
    expected_usernames = set(['dkaspar'])
    msg = {
        "i": 0,
        "timestamp": 1491924112.0,
        "msg_id": "05ddb3ff-12aa-4295-bca0-e9f77ecb0448",
        "topic": "/topic/VirtualTopic.eng.brew.import.build",
        "msg": {
            "build_id": 550553,
            "brmap": {
                "tasks/165/12990165/ghostscript-devel-9.07-26.el7.i686.rpm": 3286167,
                "tasks/157/12990157/ghostscript-debuginfo-9.07-26.el7.x86_64.rpm": 3286166,
                "tasks/166/12990166/ghostscript-9.07-26.el7.s390x.rpm": 3286177,
                "tasks/156/12990156/ghostscript-cups-9.07-26.el7.ppc.rpm": 3286169,
                "tasks/160/12990160/ghostscript-cups-9.07-26.el7.s390.rpm": 3286173,
                "tasks/163/12990163/ghostscript-debuginfo-9.07-26.el7.ppc64le.rpm": 3286175,
                "tasks/164/12990164/ghostscript-debuginfo-9.07-26.el7.ppc64.rpm": 3286170,
                "tasks/166/12990166/ghostscript-gtk-9.07-26.el7.s390x.rpm": 3286177,
                "tasks/156/12990156/ghostscript-9.07-26.el7.ppc.rpm": 3286169,
                "tasks/160/12990160/ghostscript-devel-9.07-26.el7.s390.rpm": 3286173,
                "tasks/157/12990157/ghostscript-gtk-9.07-26.el7.x86_64.rpm": 3286166,
                "tasks/165/12990165/ghostscript-cups-9.07-26.el7.i686.rpm": 3286167,
                "tasks/162/12990162/ghostscript-cups-9.07-26.el7.aarch64.rpm": 3286168,
                "tasks/162/12990162/ghostscript-9.07-26.el7.aarch64.rpm": 3286168,
                "tasks/157/12990157/ghostscript-cups-9.07-26.el7.x86_64.rpm": 3286166,
                "tasks/160/12990160/ghostscript-9.07-26.el7.s390.rpm": 3286173,
                "tasks/165/12990165/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286167,
                "tasks/156/12990156/ghostscript-9.07-26.el7.src.rpm": 3286169,
                "tasks/165/12990165/ghostscript-gtk-9.07-26.el7.i686.rpm": 3286167,
                "tasks/164/12990164/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286170,
                "tasks/160/12990160/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286173,
                "tasks/163/12990163/ghostscript-cups-9.07-26.el7.ppc64le.rpm": 3286175,
                "tasks/162/12990162/ghostscript-devel-9.07-26.el7.aarch64.rpm": 3286168,
                "tasks/164/12990164/ghostscript-gtk-9.07-26.el7.ppc64.rpm": 3286170,
                "tasks/162/12990162/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286168,
                "tasks/165/12990165/ghostscript-9.07-26.el7.i686.rpm": 3286167,
                "tasks/166/12990166/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286177,
                "tasks/165/12990165/ghostscript-debuginfo-9.07-26.el7.i686.rpm": 3286167,
                "tasks/162/12990162/ghostscript-debuginfo-9.07-26.el7.aarch64.rpm": 3286168,
                "tasks/166/12990166/ghostscript-devel-9.07-26.el7.s390x.rpm": 3286177,
                "tasks/156/12990156/ghostscript-debuginfo-9.07-26.el7.ppc.rpm": 3286169,
                "tasks/164/12990164/ghostscript-9.07-26.el7.ppc64.rpm": 3286170,
                "tasks/163/12990163/ghostscript-gtk-9.07-26.el7.ppc64le.rpm": 3286175,
                "tasks/164/12990164/ghostscript-devel-9.07-26.el7.ppc64.rpm": 3286170,
                "tasks/156/12990156/ghostscript-devel-9.07-26.el7.ppc.rpm": 3286169,
                "tasks/166/12990166/ghostscript-debuginfo-9.07-26.el7.s390x.rpm": 3286177,
                "tasks/162/12990162/ghostscript-gtk-9.07-26.el7.aarch64.rpm": 3286168,
                "tasks/160/12990160/ghostscript-debuginfo-9.07-26.el7.s390.rpm": 3286173,
                "tasks/163/12990163/ghostscript-9.07-26.el7.ppc64le.rpm": 3286175,
                "tasks/163/12990163/ghostscript-devel-9.07-26.el7.ppc64le.rpm": 3286175,
                "tasks/156/12990156/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286169,
                "tasks/156/12990156/ghostscript-gtk-9.07-26.el7.ppc.rpm": 3286169,
                "tasks/163/12990163/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286175,
                "tasks/157/12990157/ghostscript-devel-9.07-26.el7.x86_64.rpm": 3286166,
                "tasks/157/12990157/ghostscript-doc-9.07-26.el7.noarch.rpm": 3286166,
                "tasks/164/12990164/ghostscript-cups-9.07-26.el7.ppc64.rpm": 3286170,
                "tasks/166/12990166/ghostscript-cups-9.07-26.el7.s390x.rpm": 3286177,
                "tasks/160/12990160/ghostscript-gtk-9.07-26.el7.s390.rpm": 3286173,
                "tasks/157/12990157/ghostscript-9.07-26.el7.x86_64.rpm": 3286166
            },
            "logs": {
                "ppc": [
                    "tasks/156/12990156/state.log",
                    "tasks/156/12990156/build.log",
                    "tasks/156/12990156/root.log"
                ],
                "s390": [
                    "tasks/160/12990160/state.log",
                    "tasks/160/12990160/build.log",
                    "tasks/160/12990160/root.log"
                ],
                "ppc64le": [
                    "tasks/163/12990163/root.log",
                    "tasks/163/12990163/build.log",
                    "tasks/163/12990163/state.log"
                ],
                "aarch64": [
                    "tasks/162/12990162/build.log",
                    "tasks/162/12990162/state.log",
                    "tasks/162/12990162/root.log"
                ],
                "ppc64": [
                    "tasks/164/12990164/state.log",
                    "tasks/164/12990164/build.log",
                    "tasks/164/12990164/root.log"
                ],
                "i686": [
                    "tasks/165/12990165/root.log",
                    "tasks/165/12990165/build.log",
                    "tasks/165/12990165/state.log"
                ],
                "s390x": [
                    "tasks/166/12990166/state.log",
                    "tasks/166/12990166/build.log",
                    "tasks/166/12990166/root.log"
                ],
                "x86_64": [
                    "tasks/157/12990157/root.log",
                    "tasks/157/12990157/build.log",
                    "tasks/157/12990157/state.log"
                ]
            },
            "task_id": 12990126,
            "rpms": [
                "tasks/156/12990156/ghostscript-doc-9.07-26.el7.noarch.rpm",
                "tasks/156/12990156/ghostscript-cups-9.07-26.el7.ppc.rpm",
                "tasks/156/12990156/ghostscript-devel-9.07-26.el7.ppc.rpm",
                "tasks/156/12990156/ghostscript-gtk-9.07-26.el7.ppc.rpm",
                "tasks/156/12990156/ghostscript-debuginfo-9.07-26.el7.ppc.rpm",
                "tasks/156/12990156/ghostscript-9.07-26.el7.ppc.rpm",
                "tasks/157/12990157/ghostscript-cups-9.07-26.el7.x86_64.rpm",
                "tasks/157/12990157/ghostscript-devel-9.07-26.el7.x86_64.rpm",
                "tasks/157/12990157/ghostscript-9.07-26.el7.x86_64.rpm",
                "tasks/157/12990157/ghostscript-debuginfo-9.07-26.el7.x86_64.rpm",
                "tasks/157/12990157/ghostscript-gtk-9.07-26.el7.x86_64.rpm",
                "tasks/163/12990163/ghostscript-cups-9.07-26.el7.ppc64le.rpm",
                "tasks/163/12990163/ghostscript-gtk-9.07-26.el7.ppc64le.rpm",
                "tasks/163/12990163/ghostscript-9.07-26.el7.ppc64le.rpm",
                "tasks/163/12990163/ghostscript-devel-9.07-26.el7.ppc64le.rpm",
                "tasks/163/12990163/ghostscript-debuginfo-9.07-26.el7.ppc64le.rpm",
                "tasks/162/12990162/ghostscript-debuginfo-9.07-26.el7.aarch64.rpm",
                "tasks/162/12990162/ghostscript-devel-9.07-26.el7.aarch64.rpm",
                "tasks/162/12990162/ghostscript-cups-9.07-26.el7.aarch64.rpm",
                "tasks/162/12990162/ghostscript-9.07-26.el7.aarch64.rpm",
                "tasks/162/12990162/ghostscript-gtk-9.07-26.el7.aarch64.rpm",
                "tasks/164/12990164/ghostscript-devel-9.07-26.el7.ppc64.rpm",
                "tasks/164/12990164/ghostscript-debuginfo-9.07-26.el7.ppc64.rpm",
                "tasks/164/12990164/ghostscript-gtk-9.07-26.el7.ppc64.rpm",
                "tasks/164/12990164/ghostscript-cups-9.07-26.el7.ppc64.rpm",
                "tasks/164/12990164/ghostscript-9.07-26.el7.ppc64.rpm",
                "tasks/165/12990165/ghostscript-cups-9.07-26.el7.i686.rpm",
                "tasks/165/12990165/ghostscript-debuginfo-9.07-26.el7.i686.rpm",
                "tasks/165/12990165/ghostscript-9.07-26.el7.i686.rpm",
                "tasks/165/12990165/ghostscript-gtk-9.07-26.el7.i686.rpm",
                "tasks/165/12990165/ghostscript-devel-9.07-26.el7.i686.rpm",
                "tasks/160/12990160/ghostscript-9.07-26.el7.s390.rpm",
                "tasks/160/12990160/ghostscript-devel-9.07-26.el7.s390.rpm",
                "tasks/160/12990160/ghostscript-debuginfo-9.07-26.el7.s390.rpm",
                "tasks/160/12990160/ghostscript-gtk-9.07-26.el7.s390.rpm",
                "tasks/160/12990160/ghostscript-cups-9.07-26.el7.s390.rpm",
                "tasks/166/12990166/ghostscript-devel-9.07-26.el7.s390x.rpm",
                "tasks/166/12990166/ghostscript-9.07-26.el7.s390x.rpm",
                "tasks/166/12990166/ghostscript-gtk-9.07-26.el7.s390x.rpm",
                "tasks/166/12990166/ghostscript-debuginfo-9.07-26.el7.s390x.rpm",
                "tasks/166/12990166/ghostscript-cups-9.07-26.el7.s390x.rpm"
            ],
            "build": {
                "package_name": "ghostscript",
                "extra": None,
                "creation_time": "2017-04-11 15:06:25.391196",
                "completion_time": None,
                "package_id": 537,
                "id": 550553,
                "build_id": 550553,
                "state": 0,
                "source": None,
                "epoch": None,
                "version": "9.07",
                "completion_ts": None,
                "owner_id": 3066,
                "owner_name": "dkaspar",
                "nvr": "ghostscript-9.07-26.el7",
                "start_time": "2017-04-11 15:06:25.391196",
                "creation_event_id": 15402490,
                "start_ts": 1491923185.3912,
                "volume_id": 0,
                "creation_ts": 1491923185.3912,
                "name": "ghostscript",
                "task_id": 12990126,
                "volume_name": "DEFAULT",
                "release": "26.el7"
            },
            "srpm": "tasks/156/12990156/ghostscript-9.07-26.el7.src.rpm",
            "type": "build"
        }
    }

class TestBrewImportRPM(test_brew.BrewBase):
    expected_title = 'brew.import.rpm'
    expected_subti = 'systemd-devel-219-34.el7.x86_64.rpm has been imported'
    expected_packages = set(['systemd'])
    expected_usernames = set(['lnykryn'])
    msg = {
        "i": 0,
        "timestamp": 1491918957.0,
        "msg_id": "7f6c705c-8513-41a7-bf17-f56ab5c59f10",
        "topic": "/topic/VirtualTopic.eng.brew.import.rpm",
        "msg": {
            "type": "rpm",
            "fileinfo": None,
            "rpm": {
                "build_id": 550526,
                "sourcepackage": None,
                "name": "systemd-devel",
                "arch": "x86_64",
                "buildtime": 1491918212,
                "payloadhash": "9a9f00c2ea82ec63cb251fa32554fcd6",
                "epoch": None,
                "version": "219",
                "external_repo_id": 0,
                "release": "34.el7",
                "sourcerpm": "systemd-219-34.el7.src.rpm",
                "buildroot_id": 3286008,
                "id": 4637364,
                "size": 186320
            },
            "build": {
                "package_name": "systemd",
                "extra": None,
                "creation_time": "2017-04-11 13:38:40.86017",
                "completion_time": None,
                "package_id": 34071,
                "id": 550526,
                "build_id": 550526,
                "state": 0,
                "source": None,
                "epoch": None,
                "version": "219",
                "completion_ts": None,
                "owner_id": 1615,
                "owner_name": "lnykryn",
                "nvr": "systemd-219-34.el7",
                "start_time": "2017-04-11 13:38:40.86017",
                "creation_event_id": 15401837,
                "start_ts": 1491917920.86017,
                "volume_id": 0,
                "creation_ts": 1491917920.86017,
                "name": "systemd",
                "task_id": 12989147,
                "volume_name": "DEFAULT",
                "release": "34.el7"
            },
            "filepath": "/mnt/brew/work/tasks/9157/12989157/systemd-devel-219-34.el7.x86_64.rpm"
        }
    }

class TestBrewImportArchive(test_brew.BrewBase):
    expected_title = 'brew.import.archive'
    expected_subti = 'errai-ui-3.2.5.Final-redhat-1.jar from ' \
                     'org.jboss.errai-errai-parent-3.2.5.Final_redhat_1-8 has been imported'
    expected_packages = set(['org.jboss.errai-errai-parent'])
    expected_usernames = set(['anstephe'])
    msg = {
        "i": 0,
        "timestamp": 1491930018.0,
        "msg_id": "0c6e5ca8-b9ad-46f5-be91-ce430f219264",
        "topic": "/topic/VirtualTopic.eng.brew.import.archive",
        "msg": {
            "filepath": "/mnt/brew/work/tasks/1531/12991531/org/jboss/errai/errai-ui/3.2.5.Final-redhat-1/"
            "errai-ui-3.2.5.Final-redhat-1.jar",
            "build_type": "maven",
            "build": {
                "package_name": "org.jboss.errai-errai-parent",
                "extra": None,
                "creation_time": "2017-04-11 17:00:13.711461",
                "completion_time": None,
                "package_id": 19560,
                "id": 550651,
                "build_id": 550651,
                "state": 0,
                "source": None,
                "epoch": None,
                "version": "3.2.5.Final_redhat_1",
                "completion_ts": None,
                "owner_id": 3820,
                "owner_name": "anstephe",
                "nvr": "org.jboss.errai-errai-parent-3.2.5.Final_redhat_1-8",
                "start_time": "2017-04-11 17:00:13.711461",
                "creation_event_id": 15403648,
                "start_ts": 1491930013.71146,
                "volume_id": 0,
                "creation_ts": 1491930013.71146,
                "name": "org.jboss.errai-errai-parent",
                "task_id": 12991530,
                "volume_name": "DEFAULT",
                "release": "8"
            },
            "fileinfo": {},
            "type": "archive",
            "archive": {
                "build_id": 550651,
                "version": "3.2.5.Final-redhat-1",
                "type_description": "Jar file",
                "artifact_id": "errai-ui",
                "extra": None,
                "checksum": "fe1d65b3501803a612ebfcf4f6f42b6a",
                "type_id": 1,
                "filename": "errai-ui-3.2.5.Final-redhat-1.jar",
                "type_name": "jar",
                "metadata_only": False,
                "type_extensions": "jar war rar ear sar kar jdocbook jdocbook-style plugin",
                "btype": "maven",
                "checksum_type": 0,
                "btype_id": 2,
                "group_id": "org.jboss.errai",
                "buildroot_id": None,
                "id": 1859056,
                "size": 494473
            }
        }
    }

class TestBrewImportImage(test_brew.BrewBase):
    expected_title = 'brew.import.image'
    expected_subti = 'x86_64 image from rhel-guest-image-7.4-99 has been imported'
    expected_packages = set(['rhel-guest-image'])
    expected_usernames = set(['compose/rcm-compose-nightly-01.host.prod.eng.bos.redhat.com'])
    msg = {
        "i": 0,
        "timestamp": 1491926158.0,
        "msg_id": "d45ca752-1942-46b2-a9c3-51aadb47b495",
        "topic": "/topic/VirtualTopic.eng.brew.import.image",
        "msg": {
            "fullpath": "/mnt/brew/work/tasks/230/12990230/rhel-guest-image-7.4-99.x86_64.raw.xz",
            "type": "image",
            "build": {
                "package_name": "rhel-guest-image",
                "extra": None,
                "creation_time": "2017-04-11 15:12:06.983196",
                "completion_time": None,
                "package_id": 42902,
                "id": 550555,
                "build_id": 550555,
                "state": 0,
                "source": None,
                "epoch": 0,
                "version": "7.4",
                "completion_ts": None,
                "owner_id": 3641,
                "owner_name": "compose/rcm-compose-nightly-01.host.prod.eng.bos.redhat.com",
                "nvr": "rhel-guest-image-7.4-99",
                "start_time": "2017-04-11 15:12:06.983196",
                "creation_event_id": 15402549,
                "start_ts": 1491923526.9832,
                "volume_id": 0,
                "creation_ts": 1491923526.9832,
                "name": "rhel-guest-image",
                "task_id": 12990216,
                "volume_name": "DEFAULT",
                "release": "99"
            },
            "image": {
                "files": [
                    "tdl-x86_64.xml",
                    "rhel-7.4-server-kvm.ks",
                    "koji-guest-rhel-7.4-image-build-12990230-base.ks",
                    "libvirt-qcow2-x86_64.xml",
                    "rhel-guest-image-7.4-99.x86_64.qcow2",
                    "libvirt-raw-xz-x86_64.xml",
                    "rhel-guest-image-7.4-99.x86_64.raw.xz"
                ],
                "rpmlist": [
                    {
                        "name": "teamd",
                        "buildtime": 1490591341,
                        "epoch": None,
                        "version": "1.25",
                        "release": "5.el7",
                        "arch": "x86_64",
                        "payloadhash": "7c325e52cb51f8a86038d85728b589b5",
                        "size": 277765
                    },
                    {
                        "name": "grub2-common",
                        "buildtime": 1490970740,
                        "epoch": 1,
                        "version": "2.02",
                        "release": "0.53.el7",
                        "arch": "noarch",
                        "payloadhash": "923ffc8d16fc80d3dab4ff2e17cf71d8",
                        "size": 3913922
                    },
                    {
                        "name": "libunistring",
                        "buildtime": 1390744419,
                        "epoch": None,
                        "version": "0.9.3",
                        "release": "9.el7",
                        "arch": "x86_64",
                        "payloadhash": "2634a7ca66d6fae3ad80627b05bde877",
                        "size": 1145753
                    },
                    {
                        "name": "kernel-tools-libs",
                        "buildtime": 1491587215,
                        "epoch": None,
                        "version": "3.10.0",
                        "release": "646.el7",
                        "arch": "x86_64",
                        "payloadhash": "792adf2459b94af82be4cda26fbc1697",
                        "size": 18640
                    }
                ],
                "logs": [
                    "oz-x86_64.log"
                ],
                "task_id": 12990230,
                "name": "rhel-guest-image",
                "version": "7.4",
                "release": "99",
                "arch": "x86_64",
                "relpath": "tasks/230/12990230"
            }
        }
    }

class TestBrewImportCG(test_brew.BrewBase):
    expected_title = 'brew.import.cg'
    expected_subti = 'rhel7-atomic-docker-7.3-17 has been imported by a Content Generator'
    expected_packages = set(['rhel7-atomic-docker'])
    expected_usernames = set(['osbs'])
    msg = {
        "i": 0,
        "timestamp": 1491937445.0,
        "msg_id": "5fc16f0f-92f7-4638-8048-2f4d3571bc30",
        "topic": "/topic/VirtualTopic.eng.brew.import.cg",
        "msg": {
            "directory": "koji-promote/1491937471.520017.CFvOUTpZ",
            "type": "cg",
            "build": {
                "package_name": "rhel7-atomic-docker",
                "extra": {
                    "filesystem_koji_task_id": 12993952,
                    "container_koji_task_id": 12993625,
                    "image": {
                        "autorebuild": False,
                        "help": None
                    }
                },
                "creation_time": "2017-04-11 19:04:39.18265",
                "completion_time": "2017-04-11 19:04:24",
                "package_id": 61681,
                "id": 550756,
                "build_id": 550756,
                "state": 1,
                "source": "git://pkgs.devel.redhat.com/rpms/atomic-docker#6469fe553d4ca7f1f26605dee84fab5c26652481",
                "epoch": None,
                "version": "7.3",
                "completion_ts": 1491937464.0,
                "owner_id": 3436,
                "owner_name": "osbs",
                "nvr": "rhel7-atomic-docker-7.3-17",
                "start_time": "2017-04-11 18:54:05",
                "creation_event_id": 15405094,
                "start_ts": 1491936845.0,
                "volume_id": 0,
                "creation_ts": 1491937479.18265,
                "name": "rhel7-atomic-docker",
                "task_id": None,
                "volume_name": "DEFAULT",
                "release": "17"
            },
            "metadata": {
                "buildroots": [
                    {
                        "cg_id": 1,
                        "container": {
                            "type": "docker",
                            "arch": "x86_64"
                        },
                        "extra": {
                            "osbs": {
                                "build_id": "atomic-docker-unknown-14",
                                "builder_image_id": "docker-pullable://brew-pulp-docker01.web.prod."
                                "ext.phx2.redhat.com:8888/rcm/buildroot@sha256:90671a732a1b644c76fe"
                                "18ec67cb4305cd22cf7db86efaa92aed23e4e0b1f45f"
                            }
                        },
                        "content_generator": {
                            "version": "1.6.23",
                            "name": "atomic-reactor"
                        },
                        "host": {
                            "os": "rhel-7",
                            "arch": "x86_64"
                        },
                        "components": [
                            {
                                "name": "perl-TimeDate",
                                "sigmd5": "e034b23248cf3f6b6b028688f3fce41d",
                                "type": "rpm",
                                "epoch": 1,
                                "version": "2.30",
                                "signature": "199e2f91fd431d51",
                                "release": "2.el7",
                                "arch": "noarch"
                            },
                            {
                                "name": "perl-Mozilla-PublicSuffix",
                                "sigmd5": "cad070218512ed9864a895e8a58cb5b5",
                                "type": "rpm",
                                "epoch": None,
                                "version": "0.1.19",
                                "signature": None,
                                "release": "1.el7eng",
                                "arch": "noarch"
                            },
                            {
                                "name": "setup",
                                "sigmd5": "0a445b9930665e1b435ed08b792f4811",
                                "type": "rpm",
                                "epoch": None,
                                "version": "2.8.71",
                                "signature": "199e2f91fd431d51",
                                "release": "7.el7",
                                "arch": "noarch"
                            },
                            {
                                "name": "libdnf",
                                "sigmd5": "9103f02b5f7f567e17b4a6bc38a5f3cb",
                                "type": "rpm",
                                "epoch": None,
                                "version": "0.7.4",
                                "signature": "199e2f91fd431d51",
                                "release": "3.el7",
                                "arch": "x86_64"
                            }
                        ],
                        "checksum": "a2bdc7397dacb86adc8b0c775ce5ec3f",
                        "checksum_type": "md5",
                        "buildroot_id": 1
                    }
                ]
            }
        }
    }
