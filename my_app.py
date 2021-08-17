from omegaconf import DictConfig, OmegaConf
from getpaths import getpath
import hydra


file_dir = getpath()

@hydra.main(config_path=file_dir, config_name='config')
def my_app(cfg: DictConfig) -> None:
    print(cfg)
    print(OmegaConf.to_yaml(cfg))



if __name__ == "__main__":
    my_app()