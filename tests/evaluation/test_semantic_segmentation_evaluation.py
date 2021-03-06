import unittest

import numpy as np

from rastervision.core.class_map import (ClassItem, ClassMap)
from rastervision.evaluation.semantic_segmentation_evaluation import (
    SemanticSegmentationEvaluation)
from rastervision.data.label_source.semantic_segmentation_label_source import (
    SemanticSegmentationLabelSource)
from tests.mock import MockRasterSource
from tests import data_file_path


class TestSemanticSegmentationEvaluation(unittest.TestCase):
    def test_compute(self):
        class_map = ClassMap([
            ClassItem(id=1, name='one', color='#010101'),
            ClassItem(id=2, name='two', color='#020202')
        ])

        gt_array = np.ones((4, 4, 3), dtype=np.uint8)
        gt_array[0, 0, :] = 0
        gt_array[2, 2, :] = 2
        gt_raster = MockRasterSource([0, 1, 2], 3)
        gt_raster.set_raster(gt_array)
        gt_label_source = SemanticSegmentationLabelSource(
            source=gt_raster, rgb_class_map=class_map)

        p_array = np.ones((4, 4, 3), dtype=np.uint8)
        p_array[1, 1, :] = 0
        p_raster = MockRasterSource([0, 1, 2], 3)
        p_raster.set_raster(p_array)
        p_label_source = SemanticSegmentationLabelSource(
            source=p_raster, rgb_class_map=class_map)

        eval = SemanticSegmentationEvaluation(class_map)
        eval.compute(gt_label_source.get_labels(), p_label_source.get_labels())

        tp1 = 16 - 3  # 4*4 - 3 true positives for class 1
        fp1 = 1  # 1 false positive (2,2) and one don't care at (0,0)
        fn1 = 1  # one false negative (1,1)
        precision1 = float(tp1) / (tp1 + fp1)
        recall1 = float(tp1) / (tp1 + fn1)

        tp2 = 0  # 0 true positives for class 2
        fn2 = 1  # one false negative (2,2)
        precision2 = None  # float(tp2) / (tp2 + fp2) where fp2 == 0
        recall2 = float(tp2) / (tp2 + fn2)

        self.assertAlmostEqual(precision1,
                               eval.class_to_eval_item[1].precision)
        self.assertAlmostEqual(recall1, eval.class_to_eval_item[1].recall)
        self.assertEqual(precision2, eval.class_to_eval_item[2].precision)
        self.assertAlmostEqual(recall2, eval.class_to_eval_item[2].recall)

    def test_vector_compute(self):
        class_map = ClassMap([ClassItem(id=1, name='one', color='#000021')])
        gt_uri = data_file_path('3-gt-polygons.geojson')
        pred_uri = data_file_path('3-pred-polygons.geojson')

        eval = SemanticSegmentationEvaluation(class_map)
        eval.compute_vector(gt_uri, pred_uri, 'polygons', 1)

        # NOTE: The  two geojson files referenced  above contain three
        # unique geometries total, each  file contains two geometries,
        # and there is one geometry shared between the two.
        tp = 1.0
        fp = 1.0
        fn = 1.0
        precision = float(tp) / (tp + fp)
        recall = float(tp) / (tp + fn)

        self.assertAlmostEqual(precision, eval.class_to_eval_item[1].precision)
        self.assertAlmostEqual(recall, eval.class_to_eval_item[1].recall)


if __name__ == '__main__':
    unittest.main()
