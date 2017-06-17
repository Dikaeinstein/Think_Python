import time
epoch_secs = time.time() # current time since epoch
epoch_mins = epoch_secs / 60
epoch_hrs = epoch_mins / 60
epoch_days = epoch_hrs / 24
epoch_years = epoch_days / 365

hrs = 1 + (epoch_hrs % 24)
mins = (hrs % 1) * 60
secs = (mins % 1) * 60


#print(years)
print(epoch_days)
print(int(hrs), ":", int(mins), ":", int(secs))

