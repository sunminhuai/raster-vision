# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rastervision/protos/command.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from rastervision.protos import analyzer_pb2 as rastervision_dot_protos_dot_analyzer__pb2
from rastervision.protos import augmentor_pb2 as rastervision_dot_protos_dot_augmentor__pb2
from rastervision.protos import task_pb2 as rastervision_dot_protos_dot_task__pb2
from rastervision.protos import backend_pb2 as rastervision_dot_protos_dot_backend__pb2
from rastervision.protos import scene_pb2 as rastervision_dot_protos_dot_scene__pb2
from rastervision.protos import evaluator_pb2 as rastervision_dot_protos_dot_evaluator__pb2
from rastervision.protos import plugin_pb2 as rastervision_dot_protos_dot_plugin__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rastervision/protos/command.proto',
  package='rv.protos',
  syntax='proto2',
  serialized_pb=_b('\n!rastervision/protos/command.proto\x12\trv.protos\x1a\"rastervision/protos/analyzer.proto\x1a#rastervision/protos/augmentor.proto\x1a\x1erastervision/protos/task.proto\x1a!rastervision/protos/backend.proto\x1a\x1frastervision/protos/scene.proto\x1a#rastervision/protos/evaluator.proto\x1a rastervision/protos/plugin.proto\"\xb9\x0b\n\rCommandConfig\x12\x14\n\x0c\x63ommand_type\x18\x01 \x02(\t\x12\x10\n\x08root_uri\x18\x02 \x02(\t\x12@\n\x0e\x61nalyze_config\x18\x03 \x01(\x0b\x32&.rv.protos.CommandConfig.AnalyzeConfigH\x00\x12:\n\x0b\x63hip_config\x18\x04 \x01(\x0b\x32#.rv.protos.CommandConfig.ChipConfigH\x00\x12<\n\x0ctrain_config\x18\x05 \x01(\x0b\x32$.rv.protos.CommandConfig.TrainConfigH\x00\x12@\n\x0epredict_config\x18\x06 \x01(\x0b\x32&.rv.protos.CommandConfig.PredictConfigH\x00\x12:\n\x0b\x65val_config\x18\x07 \x01(\x0b\x32#.rv.protos.CommandConfig.EvalConfigH\x00\x12>\n\rbundle_config\x18\x08 \x01(\x0b\x32%.rv.protos.CommandConfig.BundleConfigH\x00\x12(\n\x07plugins\x18\t \x01(\x0b\x32\x17.rv.protos.PluginConfig\x1a\x8a\x01\n\rAnalyzeConfig\x12#\n\x04task\x18\x01 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12&\n\x06scenes\x18\x02 \x03(\x0b\x32\x16.rv.protos.SceneConfig\x12,\n\tanalyzers\x18\x03 \x03(\x0b\x32\x19.rv.protos.AnalyzerConfig\x1a\xe6\x01\n\nChipConfig\x12#\n\x04task\x18\x01 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12)\n\x07\x62\x61\x63kend\x18\x02 \x02(\x0b\x32\x18.rv.protos.BackendConfig\x12.\n\naugmentors\x18\x03 \x03(\x0b\x32\x1a.rv.protos.AugmentorConfig\x12,\n\x0ctrain_scenes\x18\x04 \x03(\x0b\x32\x16.rv.protos.SceneConfig\x12*\n\nval_scenes\x18\x05 \x03(\x0b\x32\x16.rv.protos.SceneConfig\x1a]\n\x0bTrainConfig\x12#\n\x04task\x18\x01 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12)\n\x07\x62\x61\x63kend\x18\x02 \x02(\x0b\x32\x18.rv.protos.BackendConfig\x1a\x87\x01\n\rPredictConfig\x12#\n\x04task\x18\x01 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12)\n\x07\x62\x61\x63kend\x18\x02 \x02(\x0b\x32\x18.rv.protos.BackendConfig\x12&\n\x06scenes\x18\x03 \x03(\x0b\x32\x16.rv.protos.SceneConfig\x1a\xb4\x01\n\nEvalConfig\x12#\n\x04task\x18\x01 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12)\n\x07\x62\x61\x63kend\x18\x02 \x02(\x0b\x32\x18.rv.protos.BackendConfig\x12&\n\x06scenes\x18\x03 \x03(\x0b\x32\x16.rv.protos.SceneConfig\x12.\n\nevaluators\x18\x04 \x03(\x0b\x32\x1a.rv.protos.EvaluatorConfig\x1a\xb3\x01\n\x0c\x42undleConfig\x12,\n\tanalyzers\x18\x01 \x03(\x0b\x32\x19.rv.protos.AnalyzerConfig\x12#\n\x04task\x18\x02 \x02(\x0b\x32\x15.rv.protos.TaskConfig\x12)\n\x07\x62\x61\x63kend\x18\x03 \x02(\x0b\x32\x18.rv.protos.BackendConfig\x12%\n\x05scene\x18\x04 \x02(\x0b\x32\x16.rv.protos.SceneConfigB\x10\n\x0e\x63ommand_config')
  ,
  dependencies=[rastervision_dot_protos_dot_analyzer__pb2.DESCRIPTOR,rastervision_dot_protos_dot_augmentor__pb2.DESCRIPTOR,rastervision_dot_protos_dot_task__pb2.DESCRIPTOR,rastervision_dot_protos_dot_backend__pb2.DESCRIPTOR,rastervision_dot_protos_dot_scene__pb2.DESCRIPTOR,rastervision_dot_protos_dot_evaluator__pb2.DESCRIPTOR,rastervision_dot_protos_dot_plugin__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMMANDCONFIG_ANALYZECONFIG = _descriptor.Descriptor(
  name='AnalyzeConfig',
  full_name='rv.protos.CommandConfig.AnalyzeConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.CommandConfig.AnalyzeConfig.task', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scenes', full_name='rv.protos.CommandConfig.AnalyzeConfig.scenes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analyzers', full_name='rv.protos.CommandConfig.AnalyzeConfig.analyzers', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=771,
  serialized_end=909,
)

_COMMANDCONFIG_CHIPCONFIG = _descriptor.Descriptor(
  name='ChipConfig',
  full_name='rv.protos.CommandConfig.ChipConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.CommandConfig.ChipConfig.task', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='rv.protos.CommandConfig.ChipConfig.backend', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='augmentors', full_name='rv.protos.CommandConfig.ChipConfig.augmentors', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_scenes', full_name='rv.protos.CommandConfig.ChipConfig.train_scenes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val_scenes', full_name='rv.protos.CommandConfig.ChipConfig.val_scenes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=912,
  serialized_end=1142,
)

_COMMANDCONFIG_TRAINCONFIG = _descriptor.Descriptor(
  name='TrainConfig',
  full_name='rv.protos.CommandConfig.TrainConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.CommandConfig.TrainConfig.task', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='rv.protos.CommandConfig.TrainConfig.backend', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1144,
  serialized_end=1237,
)

_COMMANDCONFIG_PREDICTCONFIG = _descriptor.Descriptor(
  name='PredictConfig',
  full_name='rv.protos.CommandConfig.PredictConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.CommandConfig.PredictConfig.task', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='rv.protos.CommandConfig.PredictConfig.backend', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scenes', full_name='rv.protos.CommandConfig.PredictConfig.scenes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1240,
  serialized_end=1375,
)

_COMMANDCONFIG_EVALCONFIG = _descriptor.Descriptor(
  name='EvalConfig',
  full_name='rv.protos.CommandConfig.EvalConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.CommandConfig.EvalConfig.task', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='rv.protos.CommandConfig.EvalConfig.backend', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scenes', full_name='rv.protos.CommandConfig.EvalConfig.scenes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evaluators', full_name='rv.protos.CommandConfig.EvalConfig.evaluators', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1378,
  serialized_end=1558,
)

_COMMANDCONFIG_BUNDLECONFIG = _descriptor.Descriptor(
  name='BundleConfig',
  full_name='rv.protos.CommandConfig.BundleConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='analyzers', full_name='rv.protos.CommandConfig.BundleConfig.analyzers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task', full_name='rv.protos.CommandConfig.BundleConfig.task', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='backend', full_name='rv.protos.CommandConfig.BundleConfig.backend', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='scene', full_name='rv.protos.CommandConfig.BundleConfig.scene', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1561,
  serialized_end=1740,
)

_COMMANDCONFIG = _descriptor.Descriptor(
  name='CommandConfig',
  full_name='rv.protos.CommandConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_type', full_name='rv.protos.CommandConfig.command_type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='root_uri', full_name='rv.protos.CommandConfig.root_uri', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='analyze_config', full_name='rv.protos.CommandConfig.analyze_config', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chip_config', full_name='rv.protos.CommandConfig.chip_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='train_config', full_name='rv.protos.CommandConfig.train_config', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='predict_config', full_name='rv.protos.CommandConfig.predict_config', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='eval_config', full_name='rv.protos.CommandConfig.eval_config', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bundle_config', full_name='rv.protos.CommandConfig.bundle_config', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='plugins', full_name='rv.protos.CommandConfig.plugins', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_COMMANDCONFIG_ANALYZECONFIG, _COMMANDCONFIG_CHIPCONFIG, _COMMANDCONFIG_TRAINCONFIG, _COMMANDCONFIG_PREDICTCONFIG, _COMMANDCONFIG_EVALCONFIG, _COMMANDCONFIG_BUNDLECONFIG, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='command_config', full_name='rv.protos.CommandConfig.command_config',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=293,
  serialized_end=1758,
)

_COMMANDCONFIG_ANALYZECONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_COMMANDCONFIG_ANALYZECONFIG.fields_by_name['scenes'].message_type = rastervision_dot_protos_dot_scene__pb2._SCENECONFIG
_COMMANDCONFIG_ANALYZECONFIG.fields_by_name['analyzers'].message_type = rastervision_dot_protos_dot_analyzer__pb2._ANALYZERCONFIG
_COMMANDCONFIG_ANALYZECONFIG.containing_type = _COMMANDCONFIG
_COMMANDCONFIG_CHIPCONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_COMMANDCONFIG_CHIPCONFIG.fields_by_name['backend'].message_type = rastervision_dot_protos_dot_backend__pb2._BACKENDCONFIG
_COMMANDCONFIG_CHIPCONFIG.fields_by_name['augmentors'].message_type = rastervision_dot_protos_dot_augmentor__pb2._AUGMENTORCONFIG
_COMMANDCONFIG_CHIPCONFIG.fields_by_name['train_scenes'].message_type = rastervision_dot_protos_dot_scene__pb2._SCENECONFIG
_COMMANDCONFIG_CHIPCONFIG.fields_by_name['val_scenes'].message_type = rastervision_dot_protos_dot_scene__pb2._SCENECONFIG
_COMMANDCONFIG_CHIPCONFIG.containing_type = _COMMANDCONFIG
_COMMANDCONFIG_TRAINCONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_COMMANDCONFIG_TRAINCONFIG.fields_by_name['backend'].message_type = rastervision_dot_protos_dot_backend__pb2._BACKENDCONFIG
_COMMANDCONFIG_TRAINCONFIG.containing_type = _COMMANDCONFIG
_COMMANDCONFIG_PREDICTCONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_COMMANDCONFIG_PREDICTCONFIG.fields_by_name['backend'].message_type = rastervision_dot_protos_dot_backend__pb2._BACKENDCONFIG
_COMMANDCONFIG_PREDICTCONFIG.fields_by_name['scenes'].message_type = rastervision_dot_protos_dot_scene__pb2._SCENECONFIG
_COMMANDCONFIG_PREDICTCONFIG.containing_type = _COMMANDCONFIG
_COMMANDCONFIG_EVALCONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_COMMANDCONFIG_EVALCONFIG.fields_by_name['backend'].message_type = rastervision_dot_protos_dot_backend__pb2._BACKENDCONFIG
_COMMANDCONFIG_EVALCONFIG.fields_by_name['scenes'].message_type = rastervision_dot_protos_dot_scene__pb2._SCENECONFIG
_COMMANDCONFIG_EVALCONFIG.fields_by_name['evaluators'].message_type = rastervision_dot_protos_dot_evaluator__pb2._EVALUATORCONFIG
_COMMANDCONFIG_EVALCONFIG.containing_type = _COMMANDCONFIG
_COMMANDCONFIG_BUNDLECONFIG.fields_by_name['analyzers'].message_type = rastervision_dot_protos_dot_analyzer__pb2._ANALYZERCONFIG
_COMMANDCONFIG_BUNDLECONFIG.fields_by_name['task'].message_type = rastervision_dot_protos_dot_task__pb2._TASKCONFIG
_COMMANDCONFIG_BUNDLECONFIG.fields_by_name['backend'].message_type = rastervision_dot_protos_dot_backend__pb2._BACKENDCONFIG
_COMMANDCONFIG_BUNDLECONFIG.fields_by_name['scene'].message_type = rastervision_dot_protos_dot_scene__pb2._SCENECONFIG
_COMMANDCONFIG_BUNDLECONFIG.containing_type = _COMMANDCONFIG
_COMMANDCONFIG.fields_by_name['analyze_config'].message_type = _COMMANDCONFIG_ANALYZECONFIG
_COMMANDCONFIG.fields_by_name['chip_config'].message_type = _COMMANDCONFIG_CHIPCONFIG
_COMMANDCONFIG.fields_by_name['train_config'].message_type = _COMMANDCONFIG_TRAINCONFIG
_COMMANDCONFIG.fields_by_name['predict_config'].message_type = _COMMANDCONFIG_PREDICTCONFIG
_COMMANDCONFIG.fields_by_name['eval_config'].message_type = _COMMANDCONFIG_EVALCONFIG
_COMMANDCONFIG.fields_by_name['bundle_config'].message_type = _COMMANDCONFIG_BUNDLECONFIG
_COMMANDCONFIG.fields_by_name['plugins'].message_type = rastervision_dot_protos_dot_plugin__pb2._PLUGINCONFIG
_COMMANDCONFIG.oneofs_by_name['command_config'].fields.append(
  _COMMANDCONFIG.fields_by_name['analyze_config'])
_COMMANDCONFIG.fields_by_name['analyze_config'].containing_oneof = _COMMANDCONFIG.oneofs_by_name['command_config']
_COMMANDCONFIG.oneofs_by_name['command_config'].fields.append(
  _COMMANDCONFIG.fields_by_name['chip_config'])
_COMMANDCONFIG.fields_by_name['chip_config'].containing_oneof = _COMMANDCONFIG.oneofs_by_name['command_config']
_COMMANDCONFIG.oneofs_by_name['command_config'].fields.append(
  _COMMANDCONFIG.fields_by_name['train_config'])
_COMMANDCONFIG.fields_by_name['train_config'].containing_oneof = _COMMANDCONFIG.oneofs_by_name['command_config']
_COMMANDCONFIG.oneofs_by_name['command_config'].fields.append(
  _COMMANDCONFIG.fields_by_name['predict_config'])
_COMMANDCONFIG.fields_by_name['predict_config'].containing_oneof = _COMMANDCONFIG.oneofs_by_name['command_config']
_COMMANDCONFIG.oneofs_by_name['command_config'].fields.append(
  _COMMANDCONFIG.fields_by_name['eval_config'])
_COMMANDCONFIG.fields_by_name['eval_config'].containing_oneof = _COMMANDCONFIG.oneofs_by_name['command_config']
_COMMANDCONFIG.oneofs_by_name['command_config'].fields.append(
  _COMMANDCONFIG.fields_by_name['bundle_config'])
_COMMANDCONFIG.fields_by_name['bundle_config'].containing_oneof = _COMMANDCONFIG.oneofs_by_name['command_config']
DESCRIPTOR.message_types_by_name['CommandConfig'] = _COMMANDCONFIG

CommandConfig = _reflection.GeneratedProtocolMessageType('CommandConfig', (_message.Message,), dict(

  AnalyzeConfig = _reflection.GeneratedProtocolMessageType('AnalyzeConfig', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDCONFIG_ANALYZECONFIG,
    __module__ = 'rastervision.protos.command_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig.AnalyzeConfig)
    ))
  ,

  ChipConfig = _reflection.GeneratedProtocolMessageType('ChipConfig', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDCONFIG_CHIPCONFIG,
    __module__ = 'rastervision.protos.command_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig.ChipConfig)
    ))
  ,

  TrainConfig = _reflection.GeneratedProtocolMessageType('TrainConfig', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDCONFIG_TRAINCONFIG,
    __module__ = 'rastervision.protos.command_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig.TrainConfig)
    ))
  ,

  PredictConfig = _reflection.GeneratedProtocolMessageType('PredictConfig', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDCONFIG_PREDICTCONFIG,
    __module__ = 'rastervision.protos.command_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig.PredictConfig)
    ))
  ,

  EvalConfig = _reflection.GeneratedProtocolMessageType('EvalConfig', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDCONFIG_EVALCONFIG,
    __module__ = 'rastervision.protos.command_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig.EvalConfig)
    ))
  ,

  BundleConfig = _reflection.GeneratedProtocolMessageType('BundleConfig', (_message.Message,), dict(
    DESCRIPTOR = _COMMANDCONFIG_BUNDLECONFIG,
    __module__ = 'rastervision.protos.command_pb2'
    # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig.BundleConfig)
    ))
  ,
  DESCRIPTOR = _COMMANDCONFIG,
  __module__ = 'rastervision.protos.command_pb2'
  # @@protoc_insertion_point(class_scope:rv.protos.CommandConfig)
  ))
_sym_db.RegisterMessage(CommandConfig)
_sym_db.RegisterMessage(CommandConfig.AnalyzeConfig)
_sym_db.RegisterMessage(CommandConfig.ChipConfig)
_sym_db.RegisterMessage(CommandConfig.TrainConfig)
_sym_db.RegisterMessage(CommandConfig.PredictConfig)
_sym_db.RegisterMessage(CommandConfig.EvalConfig)
_sym_db.RegisterMessage(CommandConfig.BundleConfig)


# @@protoc_insertion_point(module_scope)