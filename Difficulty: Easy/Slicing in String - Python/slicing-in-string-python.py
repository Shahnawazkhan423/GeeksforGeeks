# Function to join given bound_by and tag
def join_middle(bound_by, tag_name):
  # complete the statement below to return the string as required
    leng = len(bound_by)//2
    result = bound_by[0:leng] + tag_name + bound_by[leng:]
    return result