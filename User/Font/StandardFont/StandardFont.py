
from ..Font import Font as Font

class StandardFont(Font):
        def __init__(self):
            Font.m_fontType = "Standard Font"
            Font.m_fontWidth = 6
            Font.m_fontHeight = 6

            self.createFontSources()

        def matchCharacter(self, characters = str):
            sources = []
            for i in range(0, len(characters)):
                if (characters[i] in Font.m_fontSource) != True:
                    print("Couldn't find source, not available font")
                    return []
                sources.append(Font.m_fontSource[characters[i]].splitlines())
            return sources
        
        def createFontSources(self):
            Font.m_fontSource["a"] = "      \n  **  \n *  * \n*   * \n*   * \n *** *\n"
            Font.m_fontSource["b"] = "      \n *    \n *    \n **** \n *   *\n **** \n"
            Font.m_fontSource["c"] = "      \n      \n  *** \n *    \n *    \n  *** \n"
            Font.m_fontSource["d"] = "      \n    * \n    * \n **** \n*   * \n **** \n"
            Font.m_fontSource["e"] = "      \n  **  \n *  * \n **** \n *    \n  *** \n"
            Font.m_fontSource["f"] = "      \n   *  \n  *   \n **** \n  *   \n  *   \n"
            Font.m_fontSource["g"] = "      \n  **  \n *  * \n +*** \n    * \n  **  \n"
            Font.m_fontSource["h"] = "      \n *    \n *    \n ***  \n *  * \n *  * \n"
            Font.m_fontSource["i"] = "      \n   *  \n      \n   *  \n   *  \n   *  \n"
            Font.m_fontSource["j"] = "      \n   *  \n      \n   *  \n * *  \n  *   \n"
            Font.m_fontSource["k"] = "      \n *    \n *    \n * *  \n **   \n * *  \n"
            Font.m_fontSource["l"] = "      \n   *  \n   *  \n   *  \n   *  \n   *  \n"
            Font.m_fontSource["m"] = "      \n      \n  * * \n * * *\n *   *\n *   *\n"
            Font.m_fontSource["n"] = "      \n      \n  *** \n *   *\n *   *\n *   *\n"
            Font.m_fontSource["p"] = "      \n ***  \n *  * \n ***  \n *    \n *    \n"
            Font.m_fontSource["q"] = "      \n  *** \n *  * \n  *** \n    * \n    * \n"
            Font.m_fontSource["r"] = "      \n      \n * ** \n  *  *\n  *   \n  *   \n"
            Font.m_fontSource["s"] = "      \n  *** \n *    \n  **  \n    * \n  **  \n"
            Font.m_fontSource["t"] = "      \n   *  \n **** \n   *  \n   *  \n   *  \n"
            Font.m_fontSource["u"] = "      \n      \n *  * \n *  * \n *  * \n  ** *\n"
            Font.m_fontSource["v"] = "      \n      \n *   *\n *   *\n  * * \n   *  \n"
            Font.m_fontSource["w"] = "      \n      \n      \n *   *\n * * *\n  * * \n"
            Font.m_fontSource["x"] = "      \n      \n      \n  * * \n   *  \n  * * \n"
            Font.m_fontSource["y"] = "      \n *  * \n *  * \n  *** \n    * \n    * \n"
            Font.m_fontSource["z"] = "      \n **** \n    * \n   *  \n  *   \n **** \n"
            Font.m_fontSource["0"] = "      \n  **  \n *  * \n *  * \n *  * \n  **  \n"
            Font.m_fontSource["1"] = "      \n   *  \n  **  \n   *  \n   *  \n  *** \n"
            Font.m_fontSource["2"] = "      \n  **  \n *  * \n   *  \n  *   \n **** \n"
            Font.m_fontSource["3"] = "      \n  **  \n *  * \n   *  \n *  * \n  **  \n"
            Font.m_fontSource["4"] = "      \n   ** \n  * * \n **** \n    * \n    * \n"
            Font.m_fontSource["5"] = "      \n **** \n *    \n  **  \n    * \n  **  \n"
            Font.m_fontSource["6"] = "      \n  **  \n *    \n ***  \n *  * \n  **  \n"
            Font.m_fontSource["7"] = "      \n **** \n    * \n   *  \n  *   \n *    \n"
            Font.m_fontSource["8"] = "      \n  **  \n *  * \n  **  \n *  * \n  **  \n"
            Font.m_fontSource["9"] = "      \n  **  \n *  * \n  *** \n    * \n    * \n"

            # Font.m_fontSource["a"] = "======\n==**==\n=*==*=\n*===*=\n*===*=\n=***=*"
            # Font.m_fontSource["b"] = "======\n=*====\n=*====\n=****=\n=*===*\n=****=\n"
            #
            # Font.m_fontSource["c"] = "======\n======\n==***=\n=*====\n=*====\n==***=\n"
            # Font.m_fontSource["d"] = "======\n====*=\n====*=\n=****=\n*===*=\n=****=\n"
            # Font.m_fontSource["e"] = "======\n==**==\n=*==*=\n=****=\n=*====\n==***=\n"
            # Font.m_fontSource["f"] = "======\n===*==\n==*===\n=****=\n==*===\n==*===\n"
            #
            # Font.m_fontSource["g"] = "======\n==**==\n=*==*=\n=+***=\n====*=\n==**==\n"
            #
            # Font.m_fontSource["h"] = "======\n=*====\n=*====\n=***==\n=*==*=\n=*==*=\n"
            #
            # Font.m_fontSource["i"] = "======\n===*==\n======\n===*==\n===*==\n===*==\n"
            #
            # Font.m_fontSource["j"] = "======\n===*==\n======\n===*==\n=*=*==\n==*===\n"
            #
            # Font.m_fontSource["k"] = "======\n=*====\n=*====\n=*=*==\n=**===\n=*=*==\n"
            #
            # Font.m_fontSource["l"] = "======\n===*==\n===*==\n===*==\n===*==\n===*==\n"
            #
            # Font.m_fontSource["m"] = "======\n======\n==*=*=\n=*=*=*\n=*===*\n=*===*\n"
            #
            # Font.m_fontSource["n"] = "======\n======\n==***=\n=*===*\n=*===*\n=*===*\n"
            # Font.m_fontSource["p"] = "======\n=***==\n=*==*=\n=***==\n=*====\n=*====\n"
            # Font.m_fontSource["q"] = "======\n==***=\n=*==*=\n==***=\n====*=\n====*=\n"
            # Font.m_fontSource["r"] = "======\n======\n=*=**=\n==*==*\n==*===\n==*===\n"
            # Font.m_fontSource["s"] = "======\n==***=\n=*====\n==**==\n====*=\n==**==\n"
            # Font.m_fontSource["t"] = "======\n===*==\n=****=\n===*==\n===*==\n===*==\n"
            # Font.m_fontSource["u"] = "======\n======\n=*==*=\n=*==*=\n=*==*=\n==**=*\n"
            # Font.m_fontSource["v"] = "======\n======\n=*===*\n=*===*\n==*=*=\n===*==\n"
            # Font.m_fontSource["w"] = "======\n======\n======\n=*===*\n=*=*=*\n==*=*=\n"
            # Font.m_fontSource["x"] = "======\n======\n======\n==*=*=\n===*==\n==*=*=\n"
            # Font.m_fontSource["y"] = "======\n=*==*=\n=*==*=\n==***=\n====*=\n====*=\n"
            # Font.m_fontSource["z"] = "======\n=****=\n====*=\n===*==\n==*===\n=****=\n"
            # Font.m_fontSource["0"] = "======\n==**==\n=*==*=\n=*==*=\n=*==*=\n==**==\n"
            # Font.m_fontSource["1"] = "======\n===*==\n==**==\n===*==\n===*==\n==***=\n"
            # Font.m_fontSource["2"] = "======\n==**==\n=*==*=\n===*==\n==*===\n=****=\n"
            # Font.m_fontSource["3"] = "======\n==**==\n=*==*=\n===*==\n=*==*=\n==**==\n"
            # Font.m_fontSource["4"] = "======\n===**=\n==*=*=\n=****=\n====*=\n====*=\n"
            # Font.m_fontSource["5"] = "======\n=****=\n=*====\n==**==\n====*=\n==**==\n"
            # Font.m_fontSource["6"] = "======\n==**==\n=*====\n=***==\n=*==*=\n==**==\n"
            # Font.m_fontSource["7"] = "======\n=****=\n====*=\n===*==\n==*===\n=*====\n"
            # Font.m_fontSource["8"] = "======\n==**==\n=*==*=\n==**==\n=*==*=\n==**==\n"
            # Font.m_fontSource["9"] = "======\n==**==\n=*==*=\n==***=\n====*=\n====*=\n"




















