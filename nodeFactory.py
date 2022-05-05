#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import maya.cmds as mc

class NodeControl():
    def __init__(self):
        pass

    def nc_create(self,
                  desc,
                  side,
                  type,
                  customSuffix=""):
        '''
        :param side: (str), Valid sides ["L", "R", "C", ""]
        :param desc: (str), node description
        :param type: type of the created node, (str)
        '''

        if not isinstance(side, str) or side not in ["L", "R", "C", ""]:
            raise ValueError("Invalid 'Side' parameter, must be ['L', 'R', 'C' or ''] ")

        if not isinstance(type, str):
            raise ValueError("Invalid description. Check its a string.")


        # Creamos el prefijo para los sides
        if side==["L", "R", "C"]:
            side=side+"_"
        self.side=side

        # Node suffix dict
        self._node_types_dict= {
            "decomposeMatrix":"DCM",
            "joint":"JNT",
            "composeMatrix":"CMP",
            "motionPath":"MNP",
            "multDoubleLinear":"MDL",
            "transform":"TRN",
            "pairBlend":"PBL"
        }
        self.custom_suffix=customSuffix

        for t, s in self._node_types_dict.items():
            if t==type:
                self.node_type=str(t)
                if customSuffix:
                    self.node_suffix="_" + self.custom_suffix
                else:
                    self.node_suffix="_" + str(s)

        self.desc=desc

        created_node = mc.createNode(self.node_type,
                                     n=self.side+self.desc+self.node_suffix)

        return (created_node)
