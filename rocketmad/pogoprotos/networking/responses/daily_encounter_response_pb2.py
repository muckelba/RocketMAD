# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/daily_encounter_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data.capture import capture_probability_pb2 as pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2
from pogoprotos.data import pokemon_data_pb2 as pogoprotos_dot_data_dot_pokemon__data__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/daily_encounter_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n>pogoprotos/networking/responses/daily_encounter_response.proto\x12\x1fpogoprotos.networking.responses\x1a\x31pogoprotos/data/capture/capture_probability.proto\x1a\"pogoprotos/data/pokemon_data.proto\x1a\'pogoprotos/inventory/item/item_id.proto\"\x98\x03\n\x16\x44\x61ilyEncounterResponse\x12N\n\x06result\x18\x01 \x01(\x0e\x32>.pogoprotos.networking.responses.DailyEncounterResponse.Result\x12-\n\x07pokemon\x18\x02 \x01(\x0b\x32\x1c.pogoprotos.data.PokemonData\x12H\n\x13\x63\x61pture_probability\x18\x03 \x01(\x0b\x32+.pogoprotos.data.capture.CaptureProbability\x12\x36\n\x0b\x61\x63tive_item\x18\x04 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\"\n\x1a\x61rplus_attempts_until_flee\x18\x05 \x01(\x05\"Y\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x1b\n\x17\x45NCOUNTER_NOT_AVAILABLE\x10\x02\x12\x1a\n\x16POKEMON_INVENTORY_FULL\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2.DESCRIPTOR,pogoprotos_dot_data_dot_pokemon__data__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_DAILYENCOUNTERRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.DailyEncounterResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ENCOUNTER_NOT_AVAILABLE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_INVENTORY_FULL', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=547,
  serialized_end=636,
)
_sym_db.RegisterEnumDescriptor(_DAILYENCOUNTERRESPONSE_RESULT)


_DAILYENCOUNTERRESPONSE = _descriptor.Descriptor(
  name='DailyEncounterResponse',
  full_name='pogoprotos.networking.responses.DailyEncounterResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.DailyEncounterResponse.result', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon', full_name='pogoprotos.networking.responses.DailyEncounterResponse.pokemon', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='pogoprotos.networking.responses.DailyEncounterResponse.capture_probability', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_item', full_name='pogoprotos.networking.responses.DailyEncounterResponse.active_item', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='arplus_attempts_until_flee', full_name='pogoprotos.networking.responses.DailyEncounterResponse.arplus_attempts_until_flee', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _DAILYENCOUNTERRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=228,
  serialized_end=636,
)

_DAILYENCOUNTERRESPONSE.fields_by_name['result'].enum_type = _DAILYENCOUNTERRESPONSE_RESULT
_DAILYENCOUNTERRESPONSE.fields_by_name['pokemon'].message_type = pogoprotos_dot_data_dot_pokemon__data__pb2._POKEMONDATA
_DAILYENCOUNTERRESPONSE.fields_by_name['capture_probability'].message_type = pogoprotos_dot_data_dot_capture_dot_capture__probability__pb2._CAPTUREPROBABILITY
_DAILYENCOUNTERRESPONSE.fields_by_name['active_item'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
_DAILYENCOUNTERRESPONSE_RESULT.containing_type = _DAILYENCOUNTERRESPONSE
DESCRIPTOR.message_types_by_name['DailyEncounterResponse'] = _DAILYENCOUNTERRESPONSE

DailyEncounterResponse = _reflection.GeneratedProtocolMessageType('DailyEncounterResponse', (_message.Message,), dict(
  DESCRIPTOR = _DAILYENCOUNTERRESPONSE,
  __module__ = 'pogoprotos.networking.responses.daily_encounter_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.DailyEncounterResponse)
  ))
_sym_db.RegisterMessage(DailyEncounterResponse)


# @@protoc_insertion_point(module_scope)
