# coding: utf-8

"""
    websocket-gateway

    Describe the weboscket endpoints

    The version of the OpenAPI document: 0.1.0
    Contact: erebe@erebe.eu
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, Dict, Optional
from pydantic import BaseModel, Field, StrictStr, conint
from qovery-ws.models.resource_status_dto import ResourceStatusDto
from qovery-ws.models.unit_dto import UnitDto

class MetricDto(BaseModel):
    """
    MetricDto
    """
    current: conint(strict=True, ge=0) = Field(...)
    current_percent: conint(strict=True, ge=0) = Field(...)
    limit: conint(strict=True, ge=0) = Field(...)
    name: Optional[StrictStr] = None
    status: ResourceStatusDto = Field(...)
    unit: UnitDto = Field(...)
    additional_properties: Dict[str, Any] = {}
    __properties = ["current", "current_percent", "limit", "name", "status", "unit"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> MetricDto:
        """Create an instance of MetricDto from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if name (nullable) is None
        # and __fields_set__ contains the field
        if self.name is None and "name" in self.__fields_set__:
            _dict['name'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MetricDto:
        """Create an instance of MetricDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MetricDto.parse_obj(obj)

        _obj = MetricDto.parse_obj({
            "current": obj.get("current"),
            "current_percent": obj.get("current_percent"),
            "limit": obj.get("limit"),
            "name": obj.get("name"),
            "status": obj.get("status"),
            "unit": obj.get("unit")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


