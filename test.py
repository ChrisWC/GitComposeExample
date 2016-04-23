from GitCompose.branch_config import load_config
from GitCompose.type_branch import TypeBranch

config = load_config(".")
branch = TypeBranch(".", config)

for b in branch.get_subtrees():
    print "ROOT ", b.root

