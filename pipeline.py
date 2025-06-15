from kfp import dsl
from kfp.dsl import container_component

@dsl.pipeline(name='iris-classifier-pipeline')
def iris_pipeline():
    preprocess = dsl.ContainerOp(
        name='Preprocess',
        image='dhirajpatra/kfp-components:latest',
        command=['python', 'preprocess.py'],
        file_outputs={'output': '/tmp/data.pkl'}
    )

    train = dsl.ContainerOp(
        name='Train',
        image='dhirajpatra/kfp-components:latest',
        command=['python', 'train.py'],
        arguments=[],
    )
    train.after(preprocess)
