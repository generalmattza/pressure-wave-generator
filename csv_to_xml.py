def generate_ANSYS_xml_parameter(time, value, headers):

    time = ','.join(map(str, time))
    value = ','.join(map(str, value))

    return f"""<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
<ANSYS_EnggData>
    <MaterialData/>
    <ConvectionData/>
    <LoadVariationData>
        <MatML_Doc>
            <LoadVariation>
                    <BulkDetails>
                        <Name>{headers[1]}</Name>
                        <Form>
                            <Description/>
                    </Form>
                        <PropertyData property="pr1">
                            <Data format="float">{value}</Data>
                            <Qualifier>{headers[1]}</Qualifier>
                            <ParameterValue format="float" parameter="pa1">{time}</ParameterValue>
                    </PropertyData>
                </BulkDetails>
                    <Metadata>
                        <ParameterDetails id="pa1">
                            <Name>{headers[0]}</Name>
                    </ParameterDetails>
                        <PropertyDetails id="pr1">
                            <Name>{headers[1]}</Name>
                    </PropertyDetails>
                </Metadata>
            </LoadVariation>
        </MatML_Doc>
    </LoadVariationData>
    <BeamSectionData/>
</ANSYS_EnggData>
    """