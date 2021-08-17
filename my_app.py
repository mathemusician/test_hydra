from getpaths import getpath

import os
from hydra import initialize, initialize_config_module, initialize_config_dir, compose
from hydra.experimental.callback import Callback
from omegaconf import DictConfig, OmegaConf
import hydra


file_dir = getpath()



@hydra.main(config_path=file_dir, config_name='config')
def my_app_v1(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))



@hydra.main(config_path=file_dir, config_name="config")
def my_app_v2(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))



def my_app_v3():
    abs_config_dir = file_dir/'conf'
    with initialize_config_dir(config_dir=abs_config_dir):
        cfg = compose(overrides=["+db=postgresql"])
        print(cfg)



class MyCallback(Callback):
   def __init__(self, bucket: str, file_path: str) -> None:
        self.bucket = bucket
        self.file_path = file_path

   def on_job_end(self, config: DictConfig, **kwargs: any) -> None:
        print(f"Job ended,uploading...")
        # uploading...


if __name__ == "__main__":
    my_app_v1()
    my_app_v2()
    my_app_v3()

    # to try multi-run
    # run this in the terminal:
    # python3 my_app.py -m db=mysql,postgresql