# -*- coding: utf-8 -*-
## Project Models Init

###### ====== Shortcuts ====== ######
from apptools.model import db, ndb
from apptools.model import Polymodel
from apptools.model import Model, NDBModel
from apptools.model import Expando, NDBExpando


from project.mixins import UserAuditMixin
from project.mixins import CreatedModifiedMixin

from project.mixins import FormGeneratorMixin
from project.mixins import GridGeneratorMixin

SPIModel = Model
SPIPolyModel = Polymodel
SPIExpando = Expando