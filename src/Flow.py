from reader import Reader

print("Initializing Flow framework, reading configuration")

reader = Reader('conf/example.yaml')
step_library = reader.process()

print(step_library)
