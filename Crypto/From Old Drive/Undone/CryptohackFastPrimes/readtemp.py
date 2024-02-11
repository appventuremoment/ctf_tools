def get_value_from_dict(d, keys):
    temp = d.get(keys.pop(0))
    for i in keys:
        temp = temp[i]
    return temp

def get_value_from_dict(d, keys):
    return [d[x] for x in keys]

sampleDict = { 
  "class":{ 
     "student":{ 
        "name":"Mike",
        "marks":{ 
           "physics":70,
           "history":80
        }
     }
  }
}

keys = ['class', 'student', 'marks', 'history']
history_marks = get_value_from_dict(sampleDict, keys)
print(history_marks)  # Output: 80