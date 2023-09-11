-- fonte:
-- https://allaboutfpga.com/vhdl-code-for-binary-to-bcd-converter/
--
library ieee;
use ieee.std_logic_1164.all;
use ieee.std_logic_unsigned.all;

entity binariotobcd is
    generic(N: positive := 10);
    port(
        clk, reset: in std_logic;
        binary_in: in std_logic_vector(N-1 downto 0);
        bcd0, bcd1, bcd2, bcd3, bcd4: out std_logic_vector(3 downto 0)
    );
end binariotobcd ;

architecture behaviour of binariotobcd is

begin

end behaviour;
