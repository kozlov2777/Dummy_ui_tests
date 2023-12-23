class ListOfDataExplorerPage:
    TITLE = "API Data Explorer"
    DESCRIPTION = "Example of API User Data limited to 10 items per collection. Click on links to move between different data sets."
    LIST_OF_ADVERTISED_DATA = [
        "https://www.bluehost.com/?utm_medium=affiliate&irpid=105&channelid=P99C46097236S653N0B3A151D855E0000V100&utm_source=IR",
        "https://www.templatemonster.com/website-templates.php?aff=dummyapi&a_bid=9d380bcb&chan=dummyapi",
    ]
    SECTIONS = [
        "Users List",
        "Full User Profile",
        "Posts List",
        "User Posts",
        "Comments List",
        "Tag List",
        "Post by Tag",
    ]
    RESPONSE_OF_USERS_LIST = [
        "ms. Ann Mason",
        "mr. Sohan Pierre",
        "mr. Gonzaga Ribeiro",
        "mrs. Josefina Calvo",
        "mrs. Els Ijsseldijk",
        "mr. Jesus Riley",
        "mr. Andri Leclerc",
        "mr. Konsta Manninen",
        "ms. Ane Frafjord",
        "mrs. OlaÃ­ Gomes",
    ]
    RESPONSE_USERS_PROFILES = ["ms. Sara Andersen", "sara.andersen@example.com"]
    RESPONSE_POSTS_LIST = [
        [
            "ms. Vanessa Ramos",
            "Dog in a forest at sunset dog in forest with sun",
        ],
        ["mr. Cameron Mendoza", "white black and brown long coated small dog"],
    ]
    RESPONSE_USER_POSTS = [
        [
            "ms. Vanessa Ramos",
            "Dog in a forest at sunset dog in forest with sun",
        ],
        ["mr. Cameron Mendoza", "white black and brown long coated small dog"],
    ]
    RESPONSE_COMMENTS_LIST = [
        ["mrs. Anaelle Dumas", "Nice pic"],
        ["mr. Kenneth Carter", "Handsome pic!!!"],
    ]
    RESPONSE_TAGS_LIST = [["test"], ["якрутой"]]
    RESPONSE_POST_BY_TAG = [
        [
            "mr. Jan Siebert",
            "Cooling off in the fountain white and black short",
            "water",
        ],
        ["ms. Ann Mason", "dog in a dock by a lake", "water"],
    ]
