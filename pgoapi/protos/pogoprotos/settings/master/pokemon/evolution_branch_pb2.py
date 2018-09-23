# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/settings/master/pokemon/evolution_branch.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.enums import pokemon_id_pb2 as pogoprotos_dot_enums_dot_pokemon__id__pb2
from pogoprotos.inventory.item import item_id_pb2 as pogoprotos_dot_inventory_dot_item_dot_item__id__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/settings/master/pokemon/evolution_branch.proto',
  package='pogoprotos.settings.master.pokemon',
  syntax='proto3',
  serialized_pb=_b('\n9pogoprotos/settings/master/pokemon/evolution_branch.proto\x12\"pogoprotos.settings.master.pokemon\x1a!pogoprotos/enums/pokemon_id.proto\x1a\'pogoprotos/inventory/item/item_id.proto\"\xc3\x01\n\x0f\x45volutionBranch\x12.\n\tevolution\x18\x01 \x01(\x0e\x32\x1b.pogoprotos.enums.PokemonId\x12\x45\n\x1a\x65volution_item_requirement\x18\x02 \x01(\x0e\x32!.pogoprotos.inventory.item.ItemId\x12\x12\n\ncandy_cost\x18\x03 \x01(\x05\x12%\n\x1dkm_buddy_distance_requirement\x18\x04 \x01(\x02\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_enums_dot_pokemon__id__pb2.DESCRIPTOR,pogoprotos_dot_inventory_dot_item_dot_item__id__pb2.DESCRIPTOR,])




_EVOLUTIONBRANCH = _descriptor.Descriptor(
  name='EvolutionBranch',
  full_name='pogoprotos.settings.master.pokemon.EvolutionBranch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='evolution', full_name='pogoprotos.settings.master.pokemon.EvolutionBranch.evolution', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_item_requirement', full_name='pogoprotos.settings.master.pokemon.EvolutionBranch.evolution_item_requirement', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy_cost', full_name='pogoprotos.settings.master.pokemon.EvolutionBranch.candy_cost', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='km_buddy_distance_requirement', full_name='pogoprotos.settings.master.pokemon.EvolutionBranch.km_buddy_distance_requirement', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=174,
  serialized_end=369,
)

_EVOLUTIONBRANCH.fields_by_name['evolution'].enum_type = pogoprotos_dot_enums_dot_pokemon__id__pb2._POKEMONID
_EVOLUTIONBRANCH.fields_by_name['evolution_item_requirement'].enum_type = pogoprotos_dot_inventory_dot_item_dot_item__id__pb2._ITEMID
DESCRIPTOR.message_types_by_name['EvolutionBranch'] = _EVOLUTIONBRANCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EvolutionBranch = _reflection.GeneratedProtocolMessageType('EvolutionBranch', (_message.Message,), dict(
  DESCRIPTOR = _EVOLUTIONBRANCH,
  __module__ = 'pogoprotos.settings.master.pokemon.evolution_branch_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.settings.master.pokemon.EvolutionBranch)
  ))
_sym_db.RegisterMessage(EvolutionBranch)


# @@protoc_insertion_point(module_scope)
