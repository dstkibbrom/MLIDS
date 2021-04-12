all_ids = ['0CF00400', '0CF00300', '18FEF100', '1CFF6F00', '18ECFF00', '18FF8800', '18FF8400',
           '18FEE500', '18F00029', '18FEF200', '18FF7F00', '1CFF7100', '18EBFF00', '18FF8200',
           '18FF8600', '18FEDC00', '1CFF7700', '18FF8900', '18FEDF00', '18FEE900', '18FF8700',
           '18FEE700', '1CFEB300', '18FEC100', '18FEEE00', '18ECFF29', '18EBFF29', '0C000027',
           '0C000F27', '18FEF111', '0CF00203', '0CF00327', '18FF8327', '0C002927', '18FF5027',
           '18F00503', '18FF5127', '18FEED11', '18FEE617', '1CFFAA27', '18EC0027', '18EB0027']

# 332 packets in a second
# def prepare_dataset(file, inser_freq):

file = open("Arb_id_0/minatobus-candump-2019-05-08_030759.log", "r")
inser_freq=0.001
insert_every=int(332*inser_freq)
counter=0
test_data_benign = open("benign_data.txt", 'a')
test_data_attack_prep=open("test_data_attack_prep.txt", 'a')
for line in file:
    counter=counter+1
    if counter > 30000000 and counter < 33000000:
        test_data_benign.write(line)
    elif counter > 33000000 and counter < 36000000:
        test_data_attack_prep.write(line)
test_data_benign.close()



