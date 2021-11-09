import React from 'react'
import { getClassName } from '../../libs/GetCSS'
import Node from './Node'
import cs from './Nodes.module.css'

const NodesGroup = ({nodes, title}) => {
	return (
		<div>
			<h1 className={cs.nodesTitle}> {nodes.length ? title : ""} </h1>
			<div className={getClassName(["section", nodes.length && cs.nodesGroup])}>
				{
					nodes.map((node) => (
						<div key={node.id}>
							<Node node={node}/>
						</div>
					))
				}
			</div>
		</div>
	)
}

export default NodesGroup
