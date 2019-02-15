
#Stage0 += baseimage(image='nvidia/cuda:9.0-devel', _as='devel')

Stage0 += baseimage(image='nvidia/cuda:9.0-devel-centos7')

Stage0 += openmpi(cuda=True, infiniband=True, prefix='/usr/local/openmpi',
                  version='3.0.0')
