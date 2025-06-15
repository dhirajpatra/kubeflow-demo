from kfp import dsl
from kfp.dsl import container_component, Output, OutputPath, Input, InputPath, pipeline, Artifact


@container_component
def preprocess_op(output_data: Output[Artifact]):
    return dsl.ContainerSpec(
        image='dhirajpatra/kfp-components:latest',
        command=['python', 'preprocess.py'],
        args=[],
        output_artifacts={'output_data': output_data}
    )


@container_component
def train_op(input_data: Input[Artifact]):
    return dsl.ContainerSpec(
        image='dhirajpatra/kfp-components:latest',
        command=['python', 'train.py'],
        args=[],
        input_artifacts={'input_data': input_data}
    )


@pipeline(name='iris-classifier-pipeline')
def iris_pipeline():
    preprocess = preprocess_op()
    train = train_op(input_data=preprocess.outputs['output_data'])
