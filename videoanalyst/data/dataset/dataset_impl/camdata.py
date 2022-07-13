import os.path as osp
from typing import Dict

from videoanalyst.data.dataset.dataset_base import TRACK_DATASETS, DatasetBase
from videoanalyst.evaluation.got_benchmark.datasets import CamData
from videoanalyst.pipeline.utils.bbox import xywh2xyxy


@TRACK_DATASETS.register
class CamDataDataset(DatasetBase):
    r"""
    LaSOT dataset helper

    Hyper-parameters
    ----------------
    dataset_root: str
        path to root of the dataset
    subset: str
        dataset split name (train|val|test)
    ratio: float
        dataset ratio. used by sampler (data.sampler).
    max_diff: int
        maximum difference in index of a pair of sampled frames 
    check_integrity: bool
        if check integrity of dataset or not
    """
    default_hyper_params = dict(
        dataset_root="datasets/CamData",
        subset="train",
        ratio=1.0,
        max_diff=100,
        check_integrity=True,
    )

    def __init__(self, k_idx=None) -> None:
        r"""
        Create dataset with config

        Arguments
        ---------
        cfg: CfgNode
            dataset config
        """
        super().__init__()
        self._state["dataset"] = None
        self.k_idx = k_idx

    def update_params(self):
        r"""
        an interface for update params
        """
        dataset_root = osp.realpath(self._hyper_params["dataset_root"])
        subset = self._hyper_params["subset"]
        check_integrity = self._hyper_params["check_integrity"]
        self._state["dataset"] = CamData(dataset_root,
                                       subset=subset,
                                       check_integrity=check_integrity,
                                       k_idx=self.k_idx)

    def __getitem__(self, item: int) -> Dict:
        img_files, anno = self._state["dataset"][item]

        anno = xywh2xyxy(anno)
        sequence_data = dict(image=img_files, anno=anno)

        return sequence_data

    def __len__(self):
        return len(self._state["dataset"])
