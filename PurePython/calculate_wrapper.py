def get_total(visualise):
    '''
    Get the final sum from the txt_file input
    '''
    def calculate(txtfile):
        with open(txtfile, "r") as f:
            contents = f.readlines()

        sums = dict()
        for i in range(10):
            sums[f"sums_{i}"] = 0

        for content in contents[1:]:

            content = content.split(",")

            #content[0] = amount, content[1] = category index 
            content[0] = float(content[0])
            content[1] = int(content[1])
            sums[f"sums_{content[1]}"] += content[0]

        return visualise(sums)
    return calculate