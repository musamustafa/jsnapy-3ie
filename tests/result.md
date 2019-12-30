***************************** Device: tc0q10k01 *****************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 172 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 172 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 752 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 752 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 42 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
PASS | All "adjacency-state" is equal to "Up" [ 166 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 49 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 48 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 48 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 48 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 48 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 48 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: arp 
***************************** Command: show arp *****************************
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:c9:fc:55']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:ca:16:55']}' is not present in pre snapshot
FAIL | All "interface-name" is not same in pre and post snapshot [ 212 matched / 2 failed ]
***************************** Device: tc0q10k01 *****************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
ID gone missing!!!
ID list '{'id_0': ['10.160.172.215']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['10.160.173.91']}' is not present in pre snapshot
FAIL | All "session-state" is not same in pre and post snapshot [ 173 matched / 2 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Failed
bfd-sessions : Failed
Total No of tests passed: 12
Total No of tests failed: 2 
Overall Tests failed!!! 
***************************** Device: tc0q10k02 *****************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 177 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 177 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 801 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 801 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 34 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
PASS | All "adjacency-state" is equal to "Up" [ 166 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 82 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 54 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 54 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 54 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 54 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 54 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: arp 
***************************** Command: show arp *****************************
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:ca:16:55']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:c9:fc:55']}' is not present in pre snapshot
FAIL | All "interface-name" is not same in pre and post snapshot [ 318 matched / 2 failed ]
***************************** Device: tc0q10k02 *****************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
ID gone missing!!!
ID list '{'id_0': ['10.160.175.91']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['10.160.174.215']}' is not present in pre snapshot
FAIL | All "session-state" is not same in pre and post snapshot [ 182 matched / 2 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Failed
bfd-sessions : Failed
Total No of tests passed: 12
Total No of tests failed: 2 
Overall Tests failed!!! 
***************************** Device: dn2q10k01 *****************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 233 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 233 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 1342 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 1342 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 71 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
PASS | All "adjacency-state" is equal to "Up" [ 165 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 89 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 57 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 57 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 57 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 57 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 57 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: arp 
***************************** Command: show arp *****************************
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:c9:fc:55']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:ca:16:55']}' is not present in pre snapshot
FAIL | All "interface-name" is not same in pre and post snapshot [ 229 matched / 2 failed ]
***************************** Device: dn2q10k01 *****************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
ID gone missing!!!
ID list '{'id_0': ['10.160.168.215']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['10.160.169.91']}' is not present in pre snapshot
FAIL | All "session-state" is not same in pre and post snapshot [ 198 matched / 2 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Failed
bfd-sessions : Failed
Total No of tests passed: 12
Total No of tests failed: 2 
Overall Tests failed!!! 
***************************** Device: dn2q10k02 *****************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 213 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 213 matched ]
***************************** Device: dn2q10k02 *****************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 1261 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 1261 matched ]
***************************** Device: dn2q10k02 *****************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 63 matched ]
***************************** Device: dn2q10k02 *****************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
PASS | All "adjacency-state" is equal to "Up" [ 165 matched ]
***************************** Device: dn2q10k02 *****************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
FAIL !! bgp neighbor on ['172.16.231.191'] was ['Active'] and became ['Connect']
FAIL | All "peer-state" is not same in pre and post snapshot [ 75 matched / 1 failed ]
***************************** Device: dn2q10k02 *****************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 50 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 50 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 50 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 50 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 50 matched ]
***************************** Device: dn2q10k02 *****************************
Tests Included: arp 
***************************** Command: show arp *****************************
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:c9:fc:55']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['58:00:bb:ca:16:55']}' is not present in pre snapshot
FAIL | All "interface-name" is not same in pre and post snapshot [ 275 matched / 2 failed ]
***************************** Device: dn2q10k02 *****************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
ID gone missing!!!
ID list '{'id_0': ['10.160.171.91']}' is not present in pre snapshot
ID gone missing!!!
ID list '{'id_0': ['10.160.170.215']}' is not present in pre snapshot
FAIL | All "session-state" is not same in pre and post snapshot [ 191 matched / 2 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Failed
route-summary : Passed
arp : Failed
bfd-sessions : Failed
Total No of tests passed: 11
Total No of tests failed: 3 
Overall Tests failed!!! 
****************************** Device: dn2e9201 ******************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 375 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 375 matched ]
****************************** Device: dn2e9201 ******************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 1010 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 1010 matched ]
****************************** Device: dn2e9201 ******************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 13 matched ]
****************************** Device: dn2e9201 ******************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
ERROR!! Nodes are not present in given Xpath: <isis-adjacency>O
FAIL | All "adjacency-state" is not equal to "Up" [ 0 matched / 1 failed ]
****************************** Device: dn2e9201 ******************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 11 matched ]
****************************** Device: dn2e9201 ******************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 14 matched ]
****************************** Device: dn2e9201 ******************************
Tests Included: arp 
***************************** Command: show arp *****************************
PASS | All "interface-name" is same in pre and post snapshot [ 259 matched ]
****************************** Device: dn2e9201 ******************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 38 matched ]
PASS | All "session-detection-time" is same in pre and post snapshot [ 38 matched ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Failed
bgp-neighbor : Passed
route-summary : Passed
arp : Passed
bfd-sessions : Passed
Total No of tests passed: 14
Total No of tests failed: 1 
Overall Tests failed!!! 
****************************** Device: dn2e9202 ******************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 332 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 332 matched ]
****************************** Device: dn2e9202 ******************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 959 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 959 matched ]
****************************** Device: dn2e9202 ******************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 13 matched ]
****************************** Device: dn2e9202 ******************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
ERROR!! Nodes are not present in given Xpath: <isis-adjacency>O
FAIL | All "adjacency-state" is not equal to "Up" [ 0 matched / 1 failed ]
****************************** Device: dn2e9202 ******************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 11 matched ]
****************************** Device: dn2e9202 ******************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 14 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 14 matched ]
****************************** Device: dn2e9202 ******************************
Tests Included: arp 
***************************** Command: show arp *****************************
PASS | All "interface-name" is same in pre and post snapshot [ 193 matched ]
****************************** Device: dn2e9202 ******************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 38 matched ]
PASS | All "session-detection-time" is same in pre and post snapshot [ 38 matched ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Failed
bgp-neighbor : Passed
route-summary : Passed
arp : Passed
bfd-sessions : Passed
Total No of tests passed: 14
Total No of tests failed: 1 
Overall Tests failed!!! 
****************************** Device: dn2m4802 ******************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 214 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 214 matched ]
****************************** Device: dn2m4802 ******************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 193 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 193 matched ]
****************************** Device: dn2m4802 ******************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 2 matched ]
****************************** Device: dn2m4802 ******************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
ERROR!! Nodes are not present in given Xpath: <isis-adjacency>O
FAIL | All "adjacency-state" is not equal to "Up" [ 0 matched / 1 failed ]
****************************** Device: dn2m4802 ******************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 5 matched ]
****************************** Device: dn2m4802 ******************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 3 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 3 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 3 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 3 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 3 matched ]
****************************** Device: dn2m4802 ******************************
Tests Included: arp 
***************************** Command: show arp *****************************
PASS | All "interface-name" is same in pre and post snapshot [ 54 matched ]
****************************** Device: dn2m4802 ******************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 5 matched ]
PASS | All "session-detection-time" is same in pre and post snapshot [ 5 matched ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Failed
bgp-neighbor : Passed
route-summary : Passed
arp : Passed
bfd-sessions : Passed
Total No of tests passed: 14
Total No of tests failed: 1 
Overall Tests failed!!! 
****************************** Device: dn2m4804 ******************************
Tests Included: test_ifd_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 165 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 165 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: test_ifl_terse 
*********************** Command: show interfaces terse ***********************
PASS | All "oper-status" is same in pre and post snapshot [ 336 matched ]
PASS | All "admin-status" is same in pre and post snapshot [ 336 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: ospf-neighbor 
****************** Command: show ospf neighbor instance all ******************
PASS | All "ospf-neighbor-state" is same in pre and post snapshot [ 1 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: isis-adj 
************************ Command: show isis adjacency ************************
PASS | All "adjacency-state" is equal to "Up" [ 4 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: bgp-neighbor 
************************* Command: show bgp summary *************************
PASS | All "peer-state" is same in pre and post snapshot [ 133 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: route-summary 
************************ Command: show route summary ************************
PASS | All "active-route-count" is with in delta difference of 20% [ 38 matched ]
PASS | All "destination-count" is with in delta difference of 20% [ 38 matched ]
PASS | All "total-route-count" is with in delta difference of 20% [ 38 matched ]
PASS | All "holddown-route-count" is with in delta difference of 20% [ 38 matched ]
PASS | All "hidden-route-count" is with in delta difference of 20% [ 38 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: arp 
***************************** Command: show arp *****************************
PASS | All "interface-name" is same in pre and post snapshot [ 62 matched ]
****************************** Device: dn2m4804 ******************************
Tests Included: bfd-sessions 
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 105 matched ]
PASS | All "session-detection-time" is same in pre and post snapshot [ 105 matched ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Passed
bfd-sessions : Passed
Total No of tests passed: 15
Total No of tests failed: 0 
Overall Tests passed!!! 
