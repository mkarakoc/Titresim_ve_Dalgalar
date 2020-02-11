# link of the Docker container
# https://hub.docker.com/r/hesap/aimpy/tags/
# FROM hesap/aimpy:jovyan_stable_latest_20181016_1758
FROM hesap/aimpy:jovyan_stable_20200211_1142

MAINTAINER Mesut Karakoç <mesudkarakoc@gmail.com>

# becom root to change jovyan password
USER root

### password of main user is Docker!
### REF: https://stackoverflow.com/questions/28721699/root-password-inside-a-docker-container
RUN echo "jovyan:Docker!" | chpasswd

# jovyan user name somehow chosen by someone that i do not know, yet. kind of forced to use!
# REF: https://mybinder.readthedocs.io/en/latest/dockerfile.html#preparing-your-dockerfile
USER jovyan

# create flint and arb path for the container when it used by mybinder.org
# some how mybinder.org does not see .bashrc or .profile files
ENV LD_LIBRARY_PATH "${LD_LIBRARY_PATH}:/home/jovyan/pylibs/flint2:/home/jovyan/pylibs/arb"

# force the container to use bash
# REF: https://stackoverflow.com/questions/33467098/how-can-the-terminal-in-jupyter-automatically-run-bash-instead-of-sh
ENV SHELL "/bin/bash"
#ENV LANG tr_TR.UTF-8
#ENV LANG=en_US.UTF-8 dash 
ENV LANG "en_US.UTF-8 bash"
#CMD ["/bin/bash"]

# working directory
WORKDIR /home/jovyan

# add dersnotlari
USER root
ADD ./dersnotlari /home/jovyan/dersnotlari
RUN chown -R jovyan:jovyan /home/jovyan/dersnotlari
USER jovyan

# make jupyter notebooks are trusted
RUN jupyter trust /home/jovyan/dersnotlari/*.ipynb

