# Copyright (C) 2017-2020 Red Hat, Inc.
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
#           Ralph Bean <rbean@redhat.com>

from setuptools import setup, find_packages

f = open('README.rst')
long_description = f.read().strip()
long_description = long_description.split('split here', 1)[1]
f.close()

install_requires = [
    'fedmsg @ git+https://github.com/fedora-infra/fedmsg.git@develop',
]

entry_points = {
    'fedmsg.meta': [
        'brew=fedmsg_meta_umb.brew:BrewProcessor',
        'rpmdiff=fedmsg_meta_umb.rpmdiff:RPMDiffProcessor',
        'cips=fedmsg_meta_umb.cips:CIPSProcessor',
        'distgit=fedmsg_meta_umb.distgit:DistGitProcessor',
        'pub=fedmsg_meta_umb.pub:PubProcessor',
        'errata=fedmsg_meta_umb.errata:ErrataProcessor',
        'pungi=fedmsg_meta_umb.pungi:PungiProcessor',
        'distill=fedmsg_meta_umb.distill:DistillProcessor',
        'mbs=fedmsg_meta_umb.mbs:MBSProcessor',
        'rhchi=fedmsg_meta_umb.rhchi:RHCHIProcessor',
        'robosignatory=fedmsg_meta_umb.robosignatory:RobosignatoryProcessor',
        'freshmaker=fedmsg_meta_umb.freshmaker:FreshmakerProcessor',
        'odcs=fedmsg_meta_umb.odcs:ODCSProcessor',
        'resultsdb=fedmsg_meta_umb.resultsdb:ResultsDBProcessor',
        'metaxor=fedmsg_meta_umb.metaxor:MetaXORProcessor',
        'greenwave=fedmsg_meta_umb.greenwave:GreenwaveProcessor',
        'ci=fedmsg_meta_umb.ci:CIProcessor',
        'jira=fedmsg_meta_umb.jira:JIRAProcessor',
        'tower=fedmsg_meta_umb.tower:TowerProcessor',
        'pnc=fedmsg_meta_umb.pnc:ProjectNewCastleProcessor',
        'repotracker=fedmsg_meta_umb.repotracker:RepotrackerProcessor',
        'waiverdb=fedmsg_meta_umb.waiverdb:WaiverDBProcessor',
        'aqe-jenkins=fedmsg_meta_umb.aqe_jenkins:AqeJenkinsProcessor',
        'clair=fedmsg_meta_umb.clair:ClairProcessor',
        'snitch=fedmsg_meta_umb.snitch:SnitchProcessor',
        'messagebusd=fedmsg_meta_umb.messagebusd:MessagebusdProcessor',
        'cts=fedmsg_meta_umb.cts:CTSProcessor',
    ]
}

setup(
    name='fedmsg_meta_umb',
    version='0.0.4',
    description="fedmsg metadata providers for services on Red Hat's Unified Message Bus",
    long_description=long_description,
    author='Mike Bonnet',
    author_email='mikeb@redhat.com',
    url='https://github.com/release-engineering/fedmsg_meta_umb/',
    license='LGPLv2+',
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    entry_points=entry_points
)
