abi = [
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "_proxyRegistryAddress",
                "type": "address",
            },
            {"internalType": "string", "name": "_name", "type": "string"},
            {"internalType": "string", "name": "_symbol", "type": "string"},
            {
                "internalType": "string",
                "name": "__baseTokenURI",
                "type": "string",
            },
            {
                "internalType": "string",
                "name": "__contractURI",
                "type": "string",
            },
        ],
        "stateMutability": "nonpayable",
        "type": "constructor",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "approved",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256",
            },
        ],
        "name": "Approval",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "owner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "operator",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "bool",
                "name": "approved",
                "type": "bool",
            },
        ],
        "name": "ApprovalForAll",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": False,
                "internalType": "address",
                "name": "userAddress",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "address payable",
                "name": "relayerAddress",
                "type": "address",
            },
            {
                "indexed": False,
                "internalType": "bytes",
                "name": "functionSignature",
                "type": "bytes",
            },
        ],
        "name": "MetaTransactionExecuted",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "previousOwner",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "newOwner",
                "type": "address",
            },
        ],
        "name": "OwnershipTransferred",
        "type": "event",
    },
    {
        "anonymous": False,
        "inputs": [
            {
                "indexed": True,
                "internalType": "address",
                "name": "from",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "address",
                "name": "to",
                "type": "address",
            },
            {
                "indexed": True,
                "internalType": "uint256",
                "name": "tokenId",
                "type": "uint256",
            },
        ],
        "name": "Transfer",
        "type": "event",
    },
    {
        "inputs": [],
        "name": "ERC712_VERSION",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
        ],
        "name": "approve",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"}
        ],
        "name": "balanceOf",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "baseTokenURI",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes32[]", "name": "_msg", "type": "bytes32[]"}
        ],
        "name": "check_used_signed",
        "outputs": [
            {
                "components": [
                    {"internalType": "bool", "name": "_used", "type": "bool"},
                    {
                        "internalType": "uint256",
                        "name": "_index",
                        "type": "uint256",
                    },
                ],
                "internalType": "struct NFT.USEDSIGNED[]",
                "name": "",
                "type": "tuple[]",
            }
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "contractURI",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {
                "internalType": "address",
                "name": "userAddress",
                "type": "address",
            },
            {
                "internalType": "bytes",
                "name": "functionSignature",
                "type": "bytes",
            },
            {"internalType": "bytes32", "name": "sigR", "type": "bytes32"},
            {"internalType": "bytes32", "name": "sigS", "type": "bytes32"},
            {"internalType": "uint8", "name": "sigV", "type": "uint8"},
        ],
        "name": "executeMetaTransaction",
        "outputs": [{"internalType": "bytes", "name": "", "type": "bytes"}],
        "stateMutability": "payable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"}
        ],
        "name": "getApproved",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getChainId",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "getDomainSeperator",
        "outputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "user", "type": "address"}
        ],
        "name": "getNonce",
        "outputs": [
            {"internalType": "uint256", "name": "nonce", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_address", "type": "address"},
            {"internalType": "string", "name": "_str", "type": "string"},
        ],
        "name": "hash",
        "outputs": [
            {"internalType": "bytes32", "name": "", "type": "bytes32"}
        ],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "owner", "type": "address"},
            {"internalType": "address", "name": "operator", "type": "address"},
        ],
        "name": "isApprovedForAll",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256[]", "name": "time", "type": "uint256[]"},
            {"internalType": "uint8[]", "name": "v", "type": "uint8[]"},
            {"internalType": "bytes32[]", "name": "r", "type": "bytes32[]"},
            {"internalType": "bytes32[]", "name": "s", "type": "bytes32[]"},
        ],
        "name": "minit_all",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "time", "type": "uint256"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "mint",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "name",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_owner", "type": "address"}
        ],
        "name": "owned_nfts",
        "outputs": [
            {"internalType": "uint256[]", "name": "", "type": "uint256[]"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "owner",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"}
        ],
        "name": "ownerOf",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_address", "type": "address"},
            {"internalType": "string", "name": "_msg", "type": "string"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "recover",
        "outputs": [
            {"internalType": "address", "name": "", "type": "address"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
        ],
        "stateMutability": "pure",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "renounceOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
            {"internalType": "bytes", "name": "data", "type": "bytes"},
        ],
        "name": "safeTransferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "operator", "type": "address"},
            {"internalType": "bool", "name": "approved", "type": "bool"},
        ],
        "name": "setApprovalForAll",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "bytes4", "name": "interfaceId", "type": "bytes4"}
        ],
        "name": "supportsInterface",
        "outputs": [{"internalType": "bool", "name": "", "type": "bool"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "symbol",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "uint256", "name": "_tokenId", "type": "uint256"}
        ],
        "name": "tokenURI",
        "outputs": [{"internalType": "string", "name": "", "type": "string"}],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [],
        "name": "totalSupply",
        "outputs": [
            {"internalType": "uint256", "name": "", "type": "uint256"}
        ],
        "stateMutability": "view",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "from", "type": "address"},
            {"internalType": "address", "name": "to", "type": "address"},
            {"internalType": "uint256", "name": "tokenId", "type": "uint256"},
        ],
        "name": "transferFrom",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "newOwner", "type": "address"}
        ],
        "name": "transferOwnership",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function",
    },
    {
        "inputs": [
            {"internalType": "address", "name": "_address", "type": "address"},
            {"internalType": "string", "name": "_msg", "type": "string"},
            {"internalType": "uint8", "name": "v", "type": "uint8"},
            {"internalType": "bytes32", "name": "r", "type": "bytes32"},
            {"internalType": "bytes32", "name": "s", "type": "bytes32"},
        ],
        "name": "validate",
        "outputs": [
            {"internalType": "bool", "name": "", "type": "bool"},
            {"internalType": "bytes32", "name": "", "type": "bytes32"},
        ],
        "stateMutability": "view",
        "type": "function",
    },
]
contract_address = "0x5a15526870Af2851161534b470e6249f9b5ea7e8"
