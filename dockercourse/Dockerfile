FROM debian:bullseye
RUN apt update -y && apt upgrade -y && apt install python3-pip -y && apt install python3.9
RUN pip install jupyter -U && pip install jupyterlab
EXPOSE 8888
CMD jupyter-lab --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --NotebookApp.password=''
#CMD docker run -it --rm -p 8888:8888 tag-id
