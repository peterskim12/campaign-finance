__author__ = 'pkim'

import csv
import json

def main():

    exp_dict = dict()

    # load candidate data to dict
    candidate_dict = dict()
    with open('cn.txt', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            this_dict = dict()
            this_dict['candidateId'] = row[0]
            this_dict['candidateName'] = row[1]
            this_dict['candidateParty'] = row[2]
            this_dict['candidateElectionYear'] = row[3]
            this_dict['candidateOfficeState'] = row[4]
            this_dict['candidateOffice'] = row[5]
            this_dict['candidateOfficeDistrict'] = row[6]
            this_dict['incumbentChallengerStatus'] = row[7]

            candidate_dict[row[0]] = this_dict
    
    # load candidate to committee mapping to dict
    ccl_dict = dict()
    with open('ccl.txt', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            this_dict = dict()
            this_dict['candidateId'] = row[0]
            this_dict['committeeId'] = row[3]

            ccl_dict[row[3]] = this_dict
    
    # load committee data to dict
    committee_dict = dict()
    with open('cm.txt', 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            this_dict = dict()
            this_dict['committeeId'] = row[0]
            this_dict['committeeName'] = row[1]
            this_dict['committeeDesignation'] = row[8]
            this_dict['committeeType'] = row[9]
            this_dict['committeeParty'] = row[10]
            this_dict['interestGroupCategory'] = row[12]
            # if committee is tied to candidate, then join in candidate details
            if (row[0] in ccl_dict):
                candidateId = ccl_dict[row[0]]['candidateId']
                this_dict['candidate'] = candidate_dict[candidateId]

            committee_dict[row[0]] = this_dict

    # process individual contributions
    with open('itcont.txt', 'r') as f:
        with open('camfin_indiv_contrib.json', 'a') as f2:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                this_dict = dict()
                this_dict['recordNumber'] = row[20]
                # do lookup on committee
                this_dict['committee'] = committee_dict[row[0]]
                this_dict['primaryGeneralIndicator'] = row[3]
                this_dict['transactionType'] = row[5]
                this_dict['entityType'] = row[6]
                this_dict['contributorName'] = row[7]
                this_dict['contributorCity'] = row[8]
                this_dict['contributorState'] = row[9]
                this_dict['contributorZip'] = row[10]
                this_dict['contributorEmployer'] = row[11]
                this_dict['contributorOccupation'] = row[12]
                this_dict['transactionDate'] = row[13]
                this_dict['transactionAmount'] = row[14]
                this_dict['memo'] = row[19]

                json.dump(this_dict, f2)
                print('', file=f2)

    # process committee contributions
    with open('itpas2.txt', 'r') as f:
        with open('camfin_comm_contrib.json', 'a') as f2:
            reader = csv.reader(f, delimiter='|')
            for row in reader:
                this_dict = dict()
                this_dict['recordNumber'] = row[21]
                this_dict['committee'] = committee_dict[row[0]]
                this_dict['primaryGeneralIndicator'] = row[3]
                this_dict['transactionType'] = row[5]
                this_dict['entityType'] = row[6]
                this_dict['contributorName'] = row[7]
                this_dict['contributorCity'] = row[8]
                this_dict['contributorState'] = row[9]
                this_dict['contributorZip'] = row[10]
                this_dict['contributorEmployer'] = row[11]
                this_dict['contributorOccupation'] = row[12]
                this_dict['transactionDate'] = row[13]
                this_dict['transactionAmount'] = row[14]
                this_dict['memo'] = row[20]
                # if committee contribution has candidate info, do lookup and join
                if (row[16] in candidate_dict):
                    this_dict['candidate'] = candidate_dict[row[16]]

                json.dump(this_dict, f2)
                print('', file=f2)

if __name__ == '__main__':
    main()
