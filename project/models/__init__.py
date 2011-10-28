# -*- coding: utf-8 -*-
## Project Models Init

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import Polymodel as SPIPolyModel
from apptools.model import Model as SPIModel, NDBModel
from apptools.model import Expando as SPIExpandoModel, NDBExpando


from project.mixins import UserAuditMixin
from project.mixins import CreatedModifiedMixin

from project.mixins import FormGeneratorMixin
from project.mixins import GridGeneratorMixin