from xmlutil import XMLStruct
msgs_xml = '''
 <top>
  <messages>
   <message name="DEBUG_BREAKPOINT">
    <field name="descriptor">
     <start>0</start>
     <size>0x8</size>
     <description>File descriptor</description>
    </field>
    <field name="lineno">
     <start>8</start>
     <size>8</size>
     <description>Line Number</description>
    </field>
    <field name="reason">
     <start>16</start>
     <size>8</size>
     <description>Breakpoint reason ID</description>
    </field>
   </message>
   <message name="MEMORY_ALLOC">
    <field name="base_address">
     <start>0</start>
     <size>32</size>
     <description>Memory allocation base address</description>
    </field>
    <field name="length">
     <start>32</start>
     <size>32</size>
     <description>Memory block length</description>
    </field>
    <field name="mode">
     <start>64</start>
     <size>8</size>
     <description>Allocation mode</description>
    </field>
   </message>
  </messages>
 </top>
'''
top = XMLStruct(msgs_xml)
print(top)
top.messages
print("First child element with a given tag name be accessed by XML tag name using . notation:")
print(top.messages.message)
print("XML attributes can also be accessed using a . notation, and in case of ambiguity, through a dict-like access:")
print(top.messages.message.name)
print("Children be accessed as a list:")
print(list(top.messages))
print("------------")
print(top.messages.message.field)