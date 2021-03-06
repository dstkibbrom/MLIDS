#single ID prediction

import logging
from utils import frame_reader_with_time, testing_dataset_creator_with_time, bits_extractor_with_time

logging.getLogger('tensorflow').disabled = True

all_ids = ['0CF00400', '0CF00300', '18FEF100', '1CFF6F00', '18ECFF00', '18FF8800', '18FF8400',
           '18FEE500', '18F00029', '18FEF200', '18FF7F00', '1CFF7100', '18EBFF00', '18FF8200',
           '18FF8600', '18FEDC00', '1CFF7700', '18FF8900', '18FEDF00', '18FEE900', '18FF8700',
           '18FEE700', '1CFEB300', '18FEC100', '18FEEE00', '18ECFF29', '18EBFF29', '0C000027',
           '0C000F27', '18FEF111', '0CF00203', '0CF00327', '18FF8327', '0C002927', '18FF5027',
           '18F00503', '18FF5127', '18FEED11', '18FEE617', '1CFFAA27', '18EC0027', '18EB0027']


def test_each_ID(arb_index,testing_duration,attack_type,attack_freq,det_window):

    file = open('../datasets/prepared_attacks/'+attack_type+'_'+str(attack_freq)+'.txt', "r")
    test_data = frame_reader_with_time.prepare_dataset(file, det_duration=det_window, arbitration_id=all_ids[arb_index], dur_seconds=testing_duration)  # total, sequencelength, 64  # 700,68,64

    bit_0, bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8, bit_9, bit_10, bit_11, bit_12, bit_13, bit_14, bit_15, bit_16, bit_17, bit_18, \
    bit_19, bit_20, bit_21, bit_22, bit_23, bit_24, bit_25, bit_26, bit_27, bit_28, bit_29, bit_30, bit_31, bit_32, bit_33, bit_34, bit_35, bit_36, \
    bit_37, bit_38, bit_39, bit_40, bit_41, bit_42, bit_43, bit_44, bit_45, bit_46, bit_47, bit_48, bit_49, bit_50, bit_51, bit_52, bit_53, bit_54, \
    bit_55, bit_56, bit_57, bit_58, bit_59, bit_60, bit_61, bit_62, bit_63 = bits_extractor_with_time.extract_all_bits(test_data)

    input_test_data = testing_dataset_creator_with_time.ready_for_training(bit_0, bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7,
                                                                           bit_8, bit_9,
                                                                           bit_10, bit_11, bit_12, bit_13, bit_14, bit_15, bit_16,
                                                                           bit_17, bit_18,
                                                                           bit_19, bit_20, bit_21, bit_22, bit_23, bit_24, bit_25,
                                                                           bit_26, bit_27,
                                                                           bit_28, bit_29, bit_30, bit_31, bit_32, bit_33, bit_34,
                                                                           bit_35, bit_36,
                                                                           bit_37, bit_38, bit_39, bit_40, bit_41, bit_42, bit_43,
                                                                           bit_44, bit_45,
                                                                           bit_46, bit_47, bit_48, bit_49, bit_50, bit_51, bit_52,
                                                                           bit_53, bit_54,
                                                                           bit_55, bit_56, bit_57, bit_58, bit_59, bit_60, bit_61,
                                                                           bit_62, bit_63,
                                                                           arb_id=all_ids[arb_index])
    print(input_test_data)

    file=open('results/'+str(attack_type)+'_'+str(attack_freq)+'_'+str(arb_index), 'w')
    file.write(str(input_test_data)+'\n')
    file.close()

    print("+++++++++++++++++++++++++++++++++++")
    if attack_type=='insertion_attack':
        file = open("../datasets/prepared_attacks/benign_data.txt", "r")
        test_data = frame_reader_with_time.prepare_dataset(file, det_duration=det_window, arbitration_id=all_ids[arb_index], dur_seconds=testing_duration)  # total, sequencelength, 64  # 700,68,64

        bit_0, bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7, bit_8, bit_9, bit_10, bit_11, bit_12, bit_13, bit_14, bit_15, bit_16, bit_17, bit_18, \
        bit_19, bit_20, bit_21, bit_22, bit_23, bit_24, bit_25, bit_26, bit_27, bit_28, bit_29, bit_30, bit_31, bit_32, bit_33, bit_34, bit_35, bit_36, \
        bit_37, bit_38, bit_39, bit_40, bit_41, bit_42, bit_43, bit_44, bit_45, bit_46, bit_47, bit_48, bit_49, bit_50, bit_51, bit_52, bit_53, bit_54, \
        bit_55, bit_56, bit_57, bit_58, bit_59, bit_60, bit_61, bit_62, bit_63 = bits_extractor_with_time.extract_all_bits(test_data)


        input_test_data = testing_dataset_creator_with_time.ready_for_training(bit_0, bit_1, bit_2, bit_3, bit_4, bit_5, bit_6, bit_7,
                                                                               bit_8, bit_9,
                                                                               bit_10, bit_11, bit_12, bit_13, bit_14, bit_15, bit_16,
                                                                               bit_17, bit_18,
                                                                               bit_19, bit_20, bit_21, bit_22, bit_23, bit_24, bit_25,
                                                                               bit_26, bit_27,
                                                                               bit_28, bit_29, bit_30, bit_31, bit_32, bit_33, bit_34,
                                                                               bit_35, bit_36,
                                                                               bit_37, bit_38, bit_39, bit_40, bit_41, bit_42, bit_43,
                                                                               bit_44, bit_45,
                                                                               bit_46, bit_47, bit_48, bit_49, bit_50, bit_51, bit_52,
                                                                               bit_53, bit_54,
                                                                               bit_55, bit_56, bit_57, bit_58, bit_59, bit_60, bit_61,
                                                                               bit_62, bit_63,
                                                                               arb_id=all_ids[arb_index])
        file=open('results/'+str(attack_type)+'_'+str(attack_freq)+'_'+str(arb_index), 'a')
        file.write(str(input_test_data))
        file.close()
        print(input_test_data)

if __name__ == "__main__":
    # benign is giong to be checked with insertion attack only
    arb_index=8
    testing_duration=1000
    attack_type='insertion_attack'
    attack_freq=0.01
    det_window=1
    print(test_each_ID(arb_index,testing_duration,attack_type,attack_freq,det_window))