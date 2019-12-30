<h1>***************************** Device: tc0q10k01 *****************************</h1>
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
PASS | All "interface-name" is same in pre and post snapshot [ 214 matched ]
***************************** Device: tc0q10k01 *****************************
Tests Included: bfd-sessions
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 175 matched ]
FAIL !! BFD session to ['10.160.172.109'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.153'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.159'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.59'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.75'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.65'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.173.41'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.173.93'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.99'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.101'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.172.155'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.173.9'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.157'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.73'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.173.51'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.95'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.187'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.15'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.172.85'] was ['6.000'] and became ['0.900']
FAIL | All "session-detection-time" is not same in pre and post snapshot [ 156 matched / 19 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Passed
bfd-sessions : Failed
Total No of tests passed: 14
Total No of tests failed: 1 
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
PASS | All "interface-name" is same in pre and post snapshot [ 320 matched ]
***************************** Device: tc0q10k02 *****************************
Tests Included: bfd-sessions
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 184 matched ]
FAIL !! BFD session to ['10.160.174.73'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.15'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.153'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.95'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.175.93'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.159'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.101'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.157'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.109'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.75'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.65'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.99'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.175.51'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.155'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.85'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.175.79'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.187'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.174.59'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.175.41'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.175.9'] was ['6.000'] and became ['0.900']
FAIL | All "session-detection-time" is not same in pre and post snapshot [ 164 matched / 20 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Passed
bfd-sessions : Failed
Total No of tests passed: 14
Total No of tests failed: 1 
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
FAIL !! hidden route count for ['VRF_MDS_INTERNET.inet.0']  was 1.0 and became 0.0
FAIL | All "hidden-route-count" is not with in delta difference of 20% [ 56 matched / 1 failed ]
***************************** Device: dn2q10k01 *****************************
Tests Included: arp
***************************** Command: show arp *****************************
PASS | All "interface-name" is same in pre and post snapshot [ 231 matched ]
***************************** Device: dn2q10k01 *****************************
Tests Included: bfd-sessions
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 200 matched ]
FAIL !! BFD session to ['10.160.168.15'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.155'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.169.9'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.151'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.75'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.168.73'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.101'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.95'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.109'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.169.93'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.159'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.169.51'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.85'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.169.41'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.59'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.153'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.169.63'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.169.79'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.99'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.168.65'] was ['0.900'] and became ['6.000']
FAIL | All "session-detection-time" is not same in pre and post snapshot [ 180 matched / 20 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Failed
arp : Passed
bfd-sessions : Failed
Total No of tests passed: 13
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
PASS | All "peer-state" is same in pre and post snapshot [ 76 matched ]
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
ID list '{'id_0': ['4c:5e:0c:02:af:df']}' is not present in post snapshot
FAIL | All "interface-name" is not same in pre and post snapshot [ 276 matched / 1 failed ]
***************************** Device: dn2q10k02 *****************************
Tests Included: bfd-sessions
************************* Command: show bfd session *************************
PASS | All "session-state" is same in pre and post snapshot [ 193 matched ]
FAIL !! BFD session to ['10.160.170.15'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.101'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.155'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.109'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.171.41'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.171.89'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.73'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.151'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.171.93'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.75'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.171.63'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.85'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.171.51'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.159'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.170.153'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.59'] was ['6.000'] and became ['0.900']
FAIL !! BFD session to ['10.160.171.9'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.65'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.99'] was ['0.900'] and became ['6.000']
FAIL !! BFD session to ['10.160.170.95'] was ['0.900'] and became ['6.000']
FAIL | All "session-detection-time" is not same in pre and post snapshot [ 173 matched / 20 failed ]
------------------------------- Final Result!! -------------------------------
test_ifd_terse : Passed
test_ifl_terse : Passed
ospf-neighbor : Passed
isis-adj : Passed
bgp-neighbor : Passed
route-summary : Passed
arp : Failed
bfd-sessions : Failed
Total No of tests passed: 13
Total No of tests failed: 2 
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
