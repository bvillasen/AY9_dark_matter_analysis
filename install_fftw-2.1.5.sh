#!/bin/sh -e

myprefix=$HOME/apps
FFTW_VERSION="3.3.5"
# FFTW_VERSION="2.1.5"
INSTALLDIR="$myprefix/fftw-${FFTW_VERSION}"
TMP="${PWD}/tmp-fftw-${FFTW_VERSION}"
LOGFILE="${TMP}/build.log"

# bash check if directory exists
if [ -d $TMP ]; then
        echo "Directory $TMP already exists. Delete it? (y/n)"
	read answer
	if [ ${answer} = "y" ]; then
		rm -rf $TMP
	else
		echo "Program aborted."
		exit 1
	fi
fi

mkdir $TMP && cd $TMP

wget http://www.fftw.org/fftw-$FFTW_VERSION.tar.gz
gzip -dc fftw-$FFTW_VERSION.tar.gz | tar xvf -
cd fftw-$FFTW_VERSION


ENABLE_MPI="--enable-mpi"
ENABLE_OPENMP="--enable-openmp"
ENABLE_THREADS="--enable-threads"
DISABLE_SHARED="--disable-shared"

./configure --prefix=$INSTALLDIR \
  $ENABLE_MPI $ENABLE_OPENMP $ENABLE_THREADS $DISABLE_SHARED --enable-type-prefix\
  CC="mpicc" F77="mpif90" MPICC="mpicc" \
  CFLAGS="-O3" FFLAGS="-O3" \
  MPILIBS=" " 2>&1 | tee -a $LOGFILE

make -j 4 2>&1 | tee -a $LOGFILE
make install 2>&1 | tee -a $LOGFILE
