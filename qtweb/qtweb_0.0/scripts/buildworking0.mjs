// build.mjs
import fs from "fs/promises";
import path from "path";
import { __dirname } from "./cjs-helper.js";

const widgetFolderPath = path.resolve(
  __dirname,
  "..",
  "src",
  "PRT_001",
  "widget"
);
const outputFilePath = path.resolve(__dirname, "..", "src", "data.json");

async function generateData() {
  try {
    const items = await fs.readdir(widgetFolderPath);
    const data = await Promise.all(
      items.map(async (item, index) => {
        const filePath = path.join(widgetFolderPath, item);
        const code = await fs.readFile(filePath, "utf-8");
        const fileType = path.extname(item).substring(1);
        return {
          id: index + 1,
          category: "widgets",
          group: path.basename(item, path.extname(item)),
          type: "Button",
          name: `${path.basename(item, path.extname(item))} 1`,
          image: `https://media.giphy.com/media/3oKIPz3VFkF3kT5qwo/giphy.gif`,
          files: [
            {
              type: fileType,
              code,
            },
          ],
        };
      })
    );

    const jsonData = JSON.stringify(data, null, 2);
    await fs.writeFile(outputFilePath, jsonData);
    console.log("Data generated successfully.");
  } catch (error) {
    console.error("Error generating data:", error.message);
  }
}

generateData();
