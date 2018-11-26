import os
from copy import deepcopy

import rastervision as rv
from rastervision.data.label_store import (
    LabelStoreConfig, LabelStoreConfigBuilder, SemanticSegmentationRasterStore)


class SemanticSegmentationRasterStoreConfig(LabelStoreConfig):
    def __init__(self, uri=None, geojson_uri=None, rgb=False):
        super().__init__(store_type=rv.SEMANTIC_SEGMENTATION_RASTER)
        self.uri = uri
        self.geojson_uri = geojson_uri
        self.rgb = rgb

    def to_proto(self):
        msg = super().to_proto()
        if self.uri:
            msg.semantic_segmentation_raster_store.uri = self.uri
        if self.geojson_uri:
            msg.semantic_segmentation_raster_store.geojson_uri = self.geojson_uri
        msg.semantic_segmentation_raster_store.rgb = self.rgb
        return msg

    def for_prediction(self, label_uri):
        return self.to_builder() \
                   .with_uri(label_uri) \
                   .build()

    def create_store(self, task_config, extent, crs_transformer, tmp_dir):
        class_map = None
        if self.rgb:
            class_map = task_config.class_map
        affine_transform = task_config.affine_transform

        return SemanticSegmentationRasterStore(
            self.uri,
            self.geojson_uri,
            extent,
            affine_transform,
            crs_transformer,
            tmp_dir,
            class_map=class_map)

    def update_for_command(self,
                           command_type,
                           experiment_config,
                           context=None,
                           io_def=None):
        io_def = io_def or rv.core.CommandIODefinition()

        if command_type == rv.PREDICT:
            if not self.uri:
                # Construct the URI for this prediction store,
                # using the scene ID.
                root = experiment_config.predict_uri
                uri = None
                for c in context:
                    if isinstance(c, rv.SceneConfig):
                        uri = os.path.join(root, '{}.tif'.format(c.id))
                if uri:
                    self.uri = uri
                    io_def.add_output(uri)
                else:
                    raise rv.ConfigError(
                        'SemanticSegmentationRasterStoreConfig has no '
                        'URI set, and is not associated with a SceneConfig.')
            if not self.geojson_uri:  # XXX and SOMETHING
                # Construct the URI for this prediction store,
                # using the scene ID.
                root = experiment_config.predict_uri
                uri = None
                for c in context:
                    if isinstance(c, rv.SceneConfig):
                        uri = os.path.join(root, '{}.geojson'.format(c.id))
                if uri:
                    self.geojson_uri = uri
                    io_def.add_output(uri)
                else:
                    raise rv.ConfigError(
                        'SemanticSegmentationRasterStoreConfig has no '
                        'GeoJSON URI set, and is not associated with a SceneConfig.'
                    )

            io_def.add_output(self.uri)
            if self.geojson_uri:
                io_def.add_output(self.geojson_uri)

        if command_type == rv.EVAL:
            if self.uri:
                io_def.add_input(self.uri)
            else:
                msg = 'No URI set for SemanticSegmentationRasterStoreConfig'
                io_def.add_missing(msg)

            if self.geojson_uri:
                io_def.add_input(self.geojson_uri)
            else:  # XXX
                msg = 'No URI set for SemanticSegmentationRasterStoreConfig'
                io_def.add_missing(msg)

        return io_def


class SemanticSegmentationRasterStoreConfigBuilder(LabelStoreConfigBuilder):
    def __init__(self, prev=None):
        config = {}
        if prev:
            config = {
                'uri': prev.uri,
                'geojson_uri': prev.geojson_uri,
                'rgb': prev.rgb,
            }

        super().__init__(SemanticSegmentationRasterStoreConfig, config)

    def from_proto(self, msg):
        return self.with_uri(msg.semantic_segmentation_raster_store.uri) \
                   .with_geojson_uri(msg.semantic_segmentation_raster_store.geojson_uri) \
                   .with_rgb(msg.semantic_segmentation_raster_store.rgb)

    def with_uri(self, uri):
        """Set URI for a GeoTIFF used to read/write predictions."""
        b = deepcopy(self)
        b.config['uri'] = uri
        return b

    def with_geojson_uri(self, geojson_uri):
        """Set URI for a GeoJSON used to write predictions."""
        b = deepcopy(self)
        b.config['geojson_uri'] = geojson_uri
        return b

    def with_rgb(self, rgb):
        """Set flag for writing RGB data using the class map.

        Otherwise this method will write the class ID into a single band.
        """
        b = deepcopy(self)
        b.config['rgb'] = rgb
        return b
